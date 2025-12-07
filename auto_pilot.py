import json

# custom packages
from models.anthropic import claude_api

from utils.prompts import auto_pilot_prompt
from predefined_missions.return_flight import return_flight
from predefined_missions.areal_scan import areal_scan
from predefined_missions.follow_path import follow_path
from drone import Drone
from output import system_print, drone_print, init_colorama
from drone_settings import CUSTOM_WEATHER, RECORDING, AirSimNH, Coastline, CityEnviron, ZhangJiajie, MSBuild

# define some constant here
# path
VIDEO_FOLDER_PATH = "assets/large_files/videos/"
VIDEO_NAME = "coastline.mp4"
FRAME_FOLDER_PATH = "assets/large_files/airsim_frames"
TEXT_FOLDER_PATH = "assets/action_lists/"

# frame related
FPS = 20

# drone related
CURRENT_ENV = Coastline

# Mission Type
RETURN_FLIGHT = 0
SURVEILLANCE_AREA = 1
FOLLOW_PATH = 2

if __name__ == "__main__":
    drone = Drone(custom_weather=CUSTOM_WEATHER, record=RECORDING)
    init_colorama()
    if CURRENT_ENV["CUSTOM_POS"]:
        drone.set_posotion(CURRENT_ENV["INIT_X"], CURRENT_ENV["INIT_Y"],
                           CURRENT_ENV["INIT_Z"], CURRENT_ENV["INIT_YAW"])
    
    logs = ""
    while True:
        system_print("input your instruction: (type 'finish' to end the operation)")
        instruction = input()
        if instruction.lower() == "finish":
            break
        
        # add mask for abstract + scenario based command
        # filtering
        raw_filter = claude_api.instruction_filter(instruction, auto_pilot_prompt.instruction_filter_prompt)
        try:
            filter = json.loads(raw_filter)
        except json.JSONDecodeError as e:
            system_print(f"Filter response is not valid JSON: {e}\nRaw output: {raw_filter}")
            continue
        
        abstract = filter.get("abstract")
        if abstract == True:
            system_print("encountering a special type of predefined mission: ", end="")
            mission_type = filter.get("mission_type")
            
            # distributing
            if mission_type == RETURN_FLIGHT:
                system_print("Return Flight", show_role=False)
                logs = return_flight(drone, instruction, logs)
            elif mission_type == SURVEILLANCE_AREA:
                system_print("Areal Surveillance", show_role=False)
                logs = areal_scan(drone, logs)
            elif mission_type == FOLLOW_PATH:
                system_print("Follow Path", show_role=False)
                logs = follow_path(drone, instruction, logs)
            
            system_print("ALL DONE~\n")
            continue
        
        counter = 0
        threshold = 5  # after 5 re-decision making, ask user if wanted to continue
        while True:
            # VLM start planning (decision making + motion planning)
            system_print("Start thinking...")
            raw_decision = claude_api.decision_making(instruction, auto_pilot_prompt.decision_making_prompt, logs, drone.frames_queue)
            
            try:
                decision = json.loads(raw_decision)
            except json.JSONDecodeError as e:
                system_print(f"Decision response is not valid JSON: {e}\nRaw output: {raw_decision}")
                continue

            plan = decision.get("actions")
            finished = decision.get("finished")
            drone.navigation_list.append(instruction)
            logs += f"{instruction}:\n"
            drone_print(f"Done! total of {len(plan)} actions\n")
            
            num = 1
            for action in plan:
                act = action.get("action")
                params = action.get("params", {})
                
                drone_print(f"Start executing action number {num}: {act}")

                if act == "takeoff":
                    drone.takeoff(params.get("height", 30))
                    logs += f"{num}: takeoff, height: {params.get('height', 30)}\n"
                elif act == "move_forward":
                    drone.move_forward(params.get("distance", 50))
                    logs += f"{num}: move forward, distance: {params.get('distance', 50)}\n"
                elif act == "rotate":
                    drone.rotate(params.get("angle", 0))
                    logs += f"{num}: rotate, angle: {params.get('angle', 0)}\n"
                elif act == "move_vertical":
                    drone.move_vertical(params.get("height", 10))
                    logs += f"{num}: move vertically, height: {params.get('height', 10)}\n"
                elif act == "land":
                    drone.land()
                    logs += f"{num}: land\n"
                else:
                    drone_print(f"Unknown action: {act}")
                
                num += 1
                
            if finished == True:
                break
            
            counter += 1
        
            if counter >= threshold:
                # ask if user still wants to do the same instruction
                while True: 
                    drone_print("Do you still want to execute this instruction? (y to continue, n to stop)")
                    flag = input()
                    if flag == 'n':
                        finished = True
                        break
                    elif flag == 'y':
                        break
                
                counter = 0
                
            if finished == True:
                break
            
        system_print("ALL DONE~\n")
        logs += "\n"
        
    # save the logs to file
    logs = "# All The Navigation and Action recorded\n\n" + logs
    with open(TEXT_FOLDER_PATH + VIDEO_NAME.removesuffix(".mp4") + ".txt", "w", encoding="utf-8") as f:
        f.write(logs)
    
    drone.cleanup()
    system_print("operation closed~ Well done pilot!\n")
    
    if RECORDING:
        system_print("Follow the following steps to get the drone footage:")
        system_print(f"Step 1: check in {FRAME_FOLDER_PATH} to find the correct folder with current time stamp")
        system_print(f"step 2: run:\n./create_video.sh ./{FRAME_FOLDER_PATH}/<the time stamp>/images/ {FPS} {VIDEO_NAME}")