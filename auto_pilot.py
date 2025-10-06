import json

# custom packages
from models.anthropic import claude_api

from utils.prompts import auto_pilot_prompt
from drone import Drone

# define some constant here
# path
VIDEO_FOLDER_PATH = "assets/large_files/videos/"
VIDEO_NAME = "try.mp4"
FRAME_FOLDER_PATH = "assets/large_files/airsim_frames"
TEXT_FOLDER_PATH = "assets/action_lists/"

# frame related
FPS = 20

# drone related
CUSTOM_POS = False
INIT_X = 160
INIT_Y = 0
INIT_Z = -50
INIT_YAW = 160

if __name__ == "__main__":
    drone = Drone()
    if CUSTOM_POS:
        drone.set_posotion(INIT_X, INIT_Y, INIT_Z, INIT_YAW)
    
    logs = ""
    while True:
        instruction = input("input your instruction: (type 'finish' to end the operation)\n")
        if instruction.lower() == "finish":
            break
        
        # add mask for abstract + scenario based command
        # filtering
        raw_filter = claude_api.instruction_filter(instruction, auto_pilot_prompt.instruction_filter_prompt)
        try:
            filter = json.loads(raw_filter)
        except json.JSONDecodeError as e:
            print(f"Filter response is not valid JSON: {e}\nRaw output: {raw_filter}")
            continue
        
        abstract = filter.get("abstract")
        if abstract == True:
            mission_type = filter.get("mission_type")
            
            # distributing
            print(mission_type)
            continue
        
        while True:
            # VLM start planning (decision making + motion planning)
            print("Start thinking...")
            raw_decision = claude_api.decision_making(instruction, auto_pilot_prompt.decision_making_prompt, logs, drone.frames_queue)
            
            try:
                decision = json.loads(raw_decision)
            except json.JSONDecodeError as e:
                print(f"Decision response is not valid JSON: {e}\nRaw output: {raw_decision}")
                continue

            plan = decision.get("actions")
            finished = decision.get("finished")
            drone.navigation_list.append(instruction)
            logs += f"{instruction}:\n"
            print(f"Done! total of {len(plan)} actions\n")
            
            num = 1
            for action in plan:
                act = action.get("action")
                params = action.get("params", {})
                
                print(f"Start executing action number {num}: {act}")

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
                    print(f"Unknown action: {act}")
                
                num += 1
                
            if finished == True:
                break
            
            drone.take_picture()  # this is the current frame of next iteration
            
        print("ALL DONE~\n")
        logs += "\n"
        
    # save the logs to file
    logs = "# All The Navigation and Action recorded\n\n" + logs
    with open(TEXT_FOLDER_PATH + VIDEO_NAME.removesuffix(".mp4") + ".txt", "w", encoding="utf-8") as f:
        f.write(logs)
    
    drone.cleanup()
    print("operation closed~ Well done pilot!\n")
    print("Follow the following steps to get the drone footage:")
    print(f"Step 1: check in {FRAME_FOLDER_PATH} to find the correct folder with current time stamp")
    print(f"step 2: run:\n./create_video.sh ./{FRAME_FOLDER_PATH}/<the time stamp>/images/ {FPS} {VIDEO_NAME}")