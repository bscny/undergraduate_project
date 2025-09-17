import json

# custom packages
from models.anthropic import claude_api

from utils.prompts import auto_pilot_prompt
from utils.image import image_processor

from drone import Drone

# define some constant here
# path
VIDEO_FOLDER_PATH = "assets/large_files/videos/"
VIDEO_NAME = "custom.mp4"
FRAME_FOLDER_PATH = "assets/large_files/airsim_frames"

# frame related
FPS = 20

if __name__ == "__main__":
    drone = Drone()
    
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
        print(f"Done! total of {len(plan)} actions\n")
        
        num = 1
        for action in plan:
            act = action.get("action")
            params = action.get("params", {})
            
            print(f"Start executing instruction number {num}: {act}")

            if act == "takeoff":
                drone.takeoff(params.get("height", 3))
            elif act == "move_forward":
                drone.move_forward(params.get("distance", 1))
            elif act == "rotate":
                drone.rotate(params.get("angle", 0))
            elif act == "land":
                drone.land()
            else:
                print(f"Unknown action: {act}")
            
            num += 1
            
        print("ALL DONE~\n")
    
    drone.cleanup()
    print("operation closed~ Well done pilot!\n")
    print("Follow the following steps to get the drone footage:")
    print(f"Step 1: check in {FRAME_FOLDER_PATH} to find the correct folder with current time stamp")
    print(f"step 2: run:\n./create_video.sh ./{FRAME_FOLDER_PATH}/<the time stamp>/images/ {FPS} {VIDEO_NAME}")