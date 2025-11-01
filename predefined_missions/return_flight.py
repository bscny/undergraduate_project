import math
import json

from drone import Drone
from utils.prompts import scenario_prompt
from models.anthropic import claude_api
from output import drone_print

# define some private functions that is only used here:
def _normalize_angle(angle):
    """Normalize angle to [-180, 180] range."""
    while angle > 180:
        angle -= 360
    while angle < -180:
        angle += 360
    return angle

def _retrace_path(drone: Drone, logs):
    """Mode 1: Retrace the original path in reverse."""
    action_count = 0
    pending_rotation = 0  # Accumulate rotations to combine them
    
    # Reverse the action list and invert each action
    for action_dict in reversed(drone.action_list):
        action = action_dict["action"]
        
        if action == "move_forward":
            # Rotate 180 degrees to face the opposite direction
            pending_rotation += 180
            
            # Normalize angle
            pending_rotation = _normalize_angle(pending_rotation)

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
        pending_rotation = _normalize_angle(pending_rotation)
        
        drone.rotate(pending_rotation)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {pending_rotation:.3f}\n"
    
    return logs


def _fly_direct(drone: Drone, logs):
    """Mode 2: Fly directly towards takeoff position."""
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
    face_angle = _normalize_angle(face_angle)
        
    drone.rotate(face_angle)
    logs += f"1: rotate, angle: {face_angle:.3f}\n"
    
    # Move forward to return to start
    drone.move_forward(return_distance)
    logs += f"2: move forward, distance: {return_distance:.3f}\n"
    
    # Rotate back to original orientation (reverse total rotation)
    final_rotation = -(180 + return_angle)
    # Normalize angle
    final_rotation = _normalize_angle(final_rotation)
        
    drone.rotate(final_rotation)
    logs += f"3: rotate, angle: {final_rotation:.3f}\n"
    
    # Height management
    if total_vertical != 0:
        drone.move_vertical(-total_vertical)
        logs += f"4: move vertically, height: {-total_vertical:.2f}\n"
    
    return logs

# main function called
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
        logs = _retrace_path(drone, logs)
    elif mode == 2:  # fly directly towards takeoff position
        logs = _fly_direct(drone, logs)
    
    return logs + "\n"