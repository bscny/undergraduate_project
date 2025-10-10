import math
import json

from drone import Drone
from utils.prompts import scenario_prompt
from models.anthropic import claude_api
from output import system_print, drone_print

def return_flight(drone: Drone, instruction, logs):
    drone.check_takeoff()
    
    talk = []
    talk.append({
        "type": "text",
        "text": scenario_prompt.return_flight_mode_prompt
    })
    talk.append({
        "type": "text",
        "text": instruction
    })
    
    # Clearify which fly back mode to use
    while True:
        raw_res = claude_api.conversation(talk)
        
        try:
            res = json.loads(raw_res)
        except json.JSONDecodeError as e:
            talk.append({
                "type": "text",
                "text": raw_res
            })
            drone_print(f"{raw_res}")
            info = input()
            talk.append({
                "type": "text",
                "text": info
            })
            continue
        
        mode = res["mode"]
        break
    
    logs += f"[Special Predefined mission]: Return Flight\n"
    
    if mode == 1:  # retrace the original path
        # Reverse the action list and invert each action       
        action_count = 0
        pending_rotation = 0  # Accumulate rotations to combine them
        
        for action_dict in reversed(drone.action_list):
            action = action_dict["action"]
            
            if action == "move_forward":
                # Rotate 180 degrees to face the opposite direction
                pending_rotation += 180
                
                # Normalize angle
                while pending_rotation > 180:
                    pending_rotation -= 360
                while pending_rotation < -180:
                    pending_rotation += 360

                # Execute the accumulated rotation
                if pending_rotation != 0:
                    drone.rotate(pending_rotation)
                    action_count += 1
                    logs += f"{action_count}: rotate, angle: {pending_rotation:.2f}\n"
                    pending_rotation = 0
                
                # Move forward the same distance
                distance = action_dict["params"]["distance"]
                drone.move_forward(distance)
                action_count += 1
                logs += f"{action_count}: move forward, distance: {distance:.2f}\n"
                
                # Add 180 degrees back to pending rotation
                pending_rotation += 180
                
            elif action == "rotate":
                # Accumulate the opposite rotation
                angle = action_dict["params"]["angle"]
                pending_rotation -= angle
        
        # Execute any remaining rotation at the end
        if pending_rotation != 0:
            # Normalize angle
            while pending_rotation > 180:
                pending_rotation -= 360
            while pending_rotation < -180:
                pending_rotation += 360
            
            drone.rotate(pending_rotation)
            action_count += 1
            logs += f"{action_count}: rotate, angle: {pending_rotation:.3f}\n"
    elif mode == 2:  # fly directly towards takeoff position
        # Initialize displacement and rotation
        total_x = 0  # forward/backward in body frame
        total_y = 0  # left/right in body frame
        total_angle = 0  # cumulative rotation
        
        # Process each action to calculate net displacement
        for action_dict in drone.action_list:
            action = action_dict["action"]
            
            if action == "move_forward":
                distance = action_dict["params"]["distance"]
                # Convert body frame movement to world frame using current rotation
                angle_rad = math.radians(total_angle)
                total_x += distance * math.cos(angle_rad)
                total_y += distance * math.sin(angle_rad)
                
            elif action == "rotate":
                angle = action_dict["params"]["angle"]
                total_angle += angle
        
        # Calculate polar coordinates for return flight
        return_distance = math.sqrt(total_x**2 + total_y**2)
        return_angle = math.degrees(math.atan2(total_y, total_x))
        
        # Fly back in the shortest path
        # First, rotate to face the return direction (180 degrees from displacement angle)
        face_angle = -total_angle + return_angle + 180
        # Normalize angle to [-180, 180]
        while face_angle > 180:
            face_angle -= 360
        while face_angle < -180:
            face_angle += 360
            
        drone.rotate(face_angle)
        logs += f"1: rotate, angle: {face_angle:.3f}\n"
        
        # Move forward to return to start
        drone.move_forward(return_distance)
        logs += f"2: move forward, distance: {return_distance:.3f}\n"
        
        # Rotate back to original orientation (reverse total rotation)
        final_rotation = -(180 + return_angle)
        # Normalize angle
        while final_rotation > 180:
            final_rotation -= 360
        while final_rotation < -180:
            final_rotation += 360
            
        drone.rotate(final_rotation)
        logs += f"3: rotate, angle: {final_rotation:.3f}\n"
    
    return logs + "\n"

def areal_scan(drone: Drone):
    # scan in a Grid Pattern (Lawnmower Pattern)
    # Configuration for the scan pattern
    # Calculate the optimal spacing parameters
    h_fov_radians = math.radians(drone.FOV_DEG)
    v_fov_radians = 2 * math.atan(math.tan(h_fov_radians / 2) * (drone.ORIG_HEIGHT / drone.ORIG_WIDTH))
    
    ground_width = 2 * drone.altitude * math.tan(h_fov_radians / 2)
    overlap_factor = 0.7  # 30% overlap
    
    leg_distance = 20  # Distance to fly forward on each leg (meters)
    num_legs = 5  # Number of parallel legs to fly
    spacing = ground_width * overlap_factor  # Distance between parallel legs (meters)
    
    drone.check_takeoff()
    
    # Execute the lawnmower pattern
    for i in range(num_legs):
        # Fly forward along current leg
        drone.move_forward(leg_distance)
        
        # Don't move after the last leg
        if i < num_legs - 1:
            # Determine turn direction based on which leg we're on
            if i % 2 == 0:
                # Turn right, move spacing, turn right again
                drone.rotate(90)
                drone.move_forward(spacing)
                drone.rotate(90)
            else:
                # Turn left, move spacing, turn left again
                drone.rotate(-90)
                drone.move_forward(spacing)
                drone.rotate(-90)