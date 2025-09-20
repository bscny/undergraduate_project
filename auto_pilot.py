import json

# custom packages
from models.anthropic import claude_api

from utils.prompts import auto_pilot_prompt
from utils.image import image_processor

from drone import Drone

# define some constant here
# path
VIDEO_FOLDER_PATH = "assets/large_files/videos/"
VIDEO_NAME = "simcity.mp4"
FRAME_FOLDER_PATH = "assets/large_files/airsim_frames"
TEXT_FOLDER_PATH = "assets/action_lists/"

# frame related
FPS = 20

# drone related
INIT_X = 300
INIT_Y = -830
INIT_Z = -5
INIT_YAW = 90

if __name__ == "__main__":
    drone = Drone()
    drone.set_posotion(INIT_X, INIT_Y, INIT_Z, INIT_YAW)
    
    logs = "# All The Navigation and Action recorded\n\n"
    while True:
        order = input("input your instruction: (type 'finish' to end the operation)")
        if order.lower() == "finish":
            break
        
        # VLM start planning instructions
        print("Start thinking...")
        raw_plan = claude_api.decision_making(order, auto_pilot_prompt.navigation_prompt, drone.navigation_list)
        
        try:
            plan = json.loads(raw_plan)
        except json.JSONDecodeError as e:
            print(f"Response is not valid JSON: {e}\nRaw output: {raw_plan}")
            continue
    
        drone.navigation_list.append(order)
        logs += f"{order}:\n"
        print(f"Done! total of {len(plan)} actions\n")
        
        num = 1
        for action in plan:
            act = action.get("action")
            params = action.get("params", {})
            
            print(f"Start executing instruction number {num}: {act}")

            if act == "takeoff":
                drone.takeoff(params.get("height", 3))
                logs += f"{num}: takeoff, height: {params.get('height', 3)}\n"
            elif act == "move_forward":
                drone.move_forward(params.get("distance", 1))
                logs += f"{num}: move forward, distance: {params.get('distance', 1)}\n"
            elif act == "rotate":
                drone.rotate(params.get("angle", 0))
                logs += f"{num}: rotate, angle: {params.get('angle', 0)}\n"
            elif act == "land":
                drone.land()
                logs += f"{num}: land\n"
            else:
                print(f"Unknown action: {act}")
            
            num += 1
            
        print("ALL DONE~\n")
        logs += "\n"
        
    # save the logs to 
    with open(TEXT_FOLDER_PATH + VIDEO_NAME.removesuffix(".mp4") + ".txt", "w", encoding="utf-8") as f:
        f.write(logs)
    
    drone.cleanup()
    print("operation closed~ Well done pilot!\n")
    print("Follow the following steps to get the drone footage:")
    print(f"Step 1: check in {FRAME_FOLDER_PATH} to find the correct folder with current time stamp")
    print(f"step 2: run:\n./create_video.sh ./{FRAME_FOLDER_PATH}/<the time stamp>/images/ {FPS} {VIDEO_NAME}")