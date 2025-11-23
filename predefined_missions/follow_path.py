import math
import json

from drone import Drone
from utils.prompts import scenario_prompt
from models.anthropic import claude_api
from models.openai import gpt_api
from models.google import gemini_api
from output import drone_print

def follow_path(drone: Drone, instruction, logs):
    drone.check_takeoff()
    
    # Calculate the optimal step parameters
    h_fov_radians = math.radians(drone.FOV_DEG)
    v_fov_radians = 2 * math.atan(math.tan(h_fov_radians / 2) * (drone.ORIG_HEIGHT / drone.ORIG_WIDTH))
    
    # get the true distance between the drone to the top of the frame
    half_ground_width = (drone.INIT_POS.z_val - drone.altitude) * math.tan(v_fov_radians / 2)
    distance_factor = 5
    forward_distance = half_ground_width * distance_factor  # the actual fly distance for each step
    
    drone.check_takeoff()
    logs += f"[Special Predefined mission]: Follow Path\n"
    
    # for each step, we do:
    # 1. VLM do angle corrrection
    # 2. move forward a small distance
    action_count = 0
    threshold = 10
    counter = 0
    while(True):
        raw_decision = gemini_api.path_correction(instruction, scenario_prompt.path_correction_prompt, drone.frames_queue[-1])
        
        try:
            decision = json.loads(raw_decision)
        except json.JSONDecodeError as e:
            drone_print(f"Correction response is not valid JSON: {e}\nRaw output: {raw_decision}")
            logs += "Failed"
            return logs + "\n"
        
        path_detected = decision["path_detected"]
        if not path_detected:
            drone_print(f"Mission end: {decision['reason']}")
            return logs + "\n"
        
        # testing prupose
        # with open(f"assets/observations/gemini-flash/{counter}.png", "wb") as f:
        #     f.write(drone.temp)
        #     logs += f"{counter}.png:\n"

        # correction + move
        correction = decision["angle_correction"]
        drone.rotate(correction)
        action_count += 1
        logs += f"{action_count}: rotate, angle: {correction:.2f}\n"
        
        drone.move_forward(forward_distance)
        action_count += 1
        logs += f"{action_count}: move forward, distance: {forward_distance:.2f}\n"
        
        counter += 1
        
        if counter >= threshold:
            # ask if user still wants to follow the object
            drone_print("Do you still want to follow it? (y to continue, n to stop)")
            flag = input()
            if flag == 'n':
                drone_print(f"Mission end")
                return logs + "\n"
            
            counter = 0