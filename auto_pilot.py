# custom packages
from models.anthropic import claude_api

from utils.prompts import auto_pilot_prompt

from drone import Drone

if __name__ == "__main__":
    drone = Drone()
    
    while True:
        order = input("input your instruction: (type 'finish' to end the operation)")
        if order.lower() == "finish":
            break
        
        drone.navigation_list.append(order)
        
        # VLM start planning instructions
        print("Start thinking...")
        plan = claude_api.decision_making(order, auto_pilot_prompt.navigation_prompt, drone.navigation_list)
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
            elif act == "rotate_counter_clock":
                drone.rotate_counter_clock(params.get("angle", 0))
            elif act == "land":
                drone.land()
            else:
                print(f"Unknown action: {act}")
            
            num += 1
            
        print("ALL DONE~\n")
        
    drone.cleanup()
    print("operation closed~ Well done pilot!")