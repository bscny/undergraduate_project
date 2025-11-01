import math

from drone import Drone
from input import input_scanning_area

def areal_scan(drone: Drone, logs):
    # Configuration for the scan pattern
    # Calculate the optimal spacing parameters
    h_fov_radians = math.radians(drone.FOV_DEG)
    v_fov_radians = 2 * math.atan(math.tan(h_fov_radians / 2) * (drone.ORIG_HEIGHT / drone.ORIG_WIDTH))
    
    ground_width = 2 * (drone.INIT_POS.z_val - drone.altitude) * math.tan(h_fov_radians / 2)
    overlap_factor = 0.7  # 70% overlap
    
    # flying through total of {leg_distance * (num_legs -1) * spacing} m^2 rectangle
    leg_distance = 200  # Distance to fly forward on each leg (meters)
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