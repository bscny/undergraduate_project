import math
from drone import Drone

def return_flight(drone: Drone, logs):
    drone.check_takeoff()
    
    logs += f"[Special Predefined mission]: Return Flight\n"
    
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
    
    return logs