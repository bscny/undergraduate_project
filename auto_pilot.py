import json

# custom packages
from models.anthropic import claude_api

from utils.prompts import auto_pilot_prompt
from mission import predefined_mission
from drone import Drone
from output import system_print, drone_print, init_colorama

# define some constant here
# path
VIDEO_FOLDER_PATH = "assets/large_files/videos/"
VIDEO_NAME = "private_land.mp4"
FRAME_FOLDER_PATH = "assets/large_files/airsim_frames"
TEXT_FOLDER_PATH = "assets/action_lists/"

# frame related
FPS = 20

# drone related
CUSTOM_WEATHER = False
CUSTOM_POS = True
INIT_X = 350
INIT_Y = 0
INIT_Z = -5
INIT_YAW = 47

# Mission Type
RETURN_FLIGHT = 0
SURVEILLANCE_AREA = 1

if __name__ == "__main__":
    drone = Drone(custom_weather=CUSTOM_WEATHER)
    init_colorama()
    if CUSTOM_POS:
        drone.set_posotion(INIT_X, INIT_Y, INIT_Z, INIT_YAW)
    
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
                system_print("Return Flight")
                logs = predefined_mission.return_flight(drone, instruction, logs)
            elif mission_type == SURVEILLANCE_AREA:
                system_print("Areal Surveillance")
                logs = predefined_mission.areal_scan(drone, logs)
            
            system_print("ALL DONE~\n")
            continue
        
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
            
            drone.take_picture()  # this is the current frame of next iteration
            
        system_print("ALL DONE~\n")
        logs += "\n"
        
    # save the logs to file
    logs = "# All The Navigation and Action recorded\n\n" + logs
    with open(TEXT_FOLDER_PATH + VIDEO_NAME.removesuffix(".mp4") + ".txt", "w", encoding="utf-8") as f:
        f.write(logs)
    
    drone.cleanup()
    system_print("operation closed~ Well done pilot!\n")
    system_print("Follow the following steps to get the drone footage:")
    system_print(f"Step 1: check in {FRAME_FOLDER_PATH} to find the correct folder with current time stamp")
    system_print(f"step 2: run:\n./create_video.sh ./{FRAME_FOLDER_PATH}/<the time stamp>/images/ {FPS} {VIDEO_NAME}")