import math
import json

from drone import Drone
from utils.prompts import scenario_prompt
from models.anthropic import claude_api
from input import input_scanning_area
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
            elif action == "move_vertical":
                height = action_dict["params"]["height"]
                drone.move_vertical(-height)
                action_count += 1
                logs += f"{action_count}: move vertically, height: {-height:.2f}\n"
        
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
        total_vertical = 0
        
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
            elif action == "move_vertical":
                height = action_dict["params"]["height"]
                total_vertical += height
        
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
        
        # height management
        if total_vertical != 0:
            drone.move_vertical(-total_vertical)
            logs += f"4: move vertically, height: {-total_vertical:.2f}\n"
    
    return logs + "\n"

def areal_scan(drone: Drone, logs):
    # Configuration for the scan pattern
    # Calculate the optimal spacing parameters
    h_fov_radians = math.radians(drone.FOV_DEG)
    v_fov_radians = 2 * math.atan(math.tan(h_fov_radians / 2) * (drone.ORIG_HEIGHT / drone.ORIG_WIDTH))
    
    ground_width = 2 * (drone.INIT_POS.z_val - drone.altitude) * math.tan(h_fov_radians / 2)
    overlap_factor = 0.5  # 50% overlap
    
    # flying through total of {leg_distance * (num_legs -1) * spacing} m^2 rectangle
    leg_distance = 100  # Distance to fly forward on each leg (meters)
    num_legs = 4  # Number of parallel legs to fly
    spacing = ground_width * overlap_factor  # Distance between parallel legs (meters)
    
    drone.check_takeoff()
    
    # Select different areal scanning method
    scan_type = input_scanning_area()
    action_count = 0
    
    logs += f"[Special Predefined mission]: Areal Scan\n"
    
    if scan_type == 0:
        # special case, scanning around using spiral method
        # Calculate number of spiral rings based on coverage area
        max_radius = max(leg_distance / 2, spacing * (num_legs - 1) / 2)
        num_rings = int(max_radius / spacing + 0.5)
        num_L = 2 * num_rings  # 2 opposite L shapes consist of a ring
        
        # Start from center and spiral outward
        current_length = spacing
        
        for L_shape in range(num_L):
            if L_shape == 0:
                # the first L is the original place without moving
                continue
            
            drone.move_forward(current_length)
            action_count += 1
            logs += f"{action_count}: move forward, distance: {current_length:.2f}\n"
            drone.rotate(90)
            action_count += 1
            logs += f"{action_count}: rotate, angle: {90:.2f}\n"
            drone.move_forward(current_length)
            action_count += 1
            logs += f"{action_count}: move forward, distance: {current_length:.2f}\n"
            drone.rotate(90)
            action_count += 1
            logs += f"{action_count}: rotate, angle: {90:.2f}\n"
            
            # Increase length for next L shape
            current_length += spacing

        return logs + "\n"
    
    # for the rest of the options, we first move to the bottom left corner of the square
    # then face upward
    elif scan_type == 1: # scan ahead
        drone.rotate(-90)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {-90:.2f}\n"
        drone.move_forward(leg_distance / 2)
        action_count += 1
        logs += f"{action_count}: move forward, distance: {leg_distance / 2:.2f}\n"
        drone.rotate(90)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {90:.2f}\n"
    elif scan_type == 2:
        drone.rotate(90)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {90:.2f}\n"
        drone.move_forward(leg_distance / 2)
        action_count += 1
        logs += f"{action_count}: move forward, distance: {leg_distance / 2:.2f}\n"
        drone.rotate(90)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {90:.2f}\n"
    elif scan_type == 3:
        drone.rotate(180)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {180:.2f}\n"
        drone.move_forward(leg_distance / 2)
        action_count += 1
        logs += f"{action_count}: move forward, distance: {leg_distance / 2:.2f}\n"
        drone.rotate(90)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {90:.2f}\n"
    elif scan_type == 4:
        drone.move_forward(leg_distance / 2)
        action_count += 1
        logs += f"{action_count}: move forward, distance: {leg_distance / 2:.2f}\n"
        drone.rotate(90)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {90:.2f}\n"
    elif scan_type == 5:
        drone.rotate(-90)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {-90:.2f}\n"
    elif scan_type == 7:
        drone.rotate(180)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {180:.2f}\n"
    elif scan_type == 8:
        drone.rotate(90)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {90:.2f}\n"

    # Execute the lawnmower pattern
    for i in range(num_legs):
        # Fly forward along current leg
        drone.move_forward(leg_distance)
        action_count += 1
        logs += f"{action_count}: move forward, distance: {leg_distance:.2f}\n"
        
        # Don't move after the last leg
        if i < num_legs - 1:
            # Determine turn direction based on which leg we're on
            if i % 2 == 0:
                # Turn right, move spacing, turn right again
                drone.rotate(90)
                action_count += 1
                logs += f"{action_count}: rotate, angle: {90:.2f}\n"
                drone.move_forward(spacing)
                action_count += 1
                logs += f"{action_count}: move forward, distance: {spacing:.2f}\n"
                drone.rotate(90)
                action_count += 1
                logs += f"{action_count}: rotate, angle: {90:.2f}\n"
            else:
                # Turn left, move spacing, turn left again
                drone.rotate(-90)
                action_count += 1
                logs += f"{action_count}: rotate, angle: {-90:.2f}\n"
                drone.move_forward(spacing)
                action_count += 1
                logs += f"{action_count}: move forward, distance: {spacing:.2f}\n"
                drone.rotate(-90)
                action_count += 1
                logs += f"{action_count}: rotate, angle: {-90:.2f}\n"
    
    return logs + "\n"