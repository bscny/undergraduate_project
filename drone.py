import airsim
from dotenv import load_dotenv
import os

load_dotenv()

class Drone:   
    def __init__(self):
        self.client = airsim.MultirotorClient(ip=os.getenv("WINDOWS_IP"))
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        self.client.simPrintLogMessage("Hello World~~")

        # define some constant here
        self.DUR = 5  # in seconds
        self.SPEED = 1  # in meters
        self.ROTATE_SPEED = 5  # in meters
        self.INIT_POS = self.get_position()  # this has x_val, y_val, z_val
        
        # define some private variables
        self.flying = False
        self.action_list = []  # lowest level
        self.navigation_list = []  # mid level

    # BELOWS ARE MEMBER FUNCTIONS THAT CONTROL DRONE ACTIONS
    # basic actions
    def takeoff(self, height = 3):
        if height <= 0:
            print("can't fly under ground...")
            return
        
        if self.flying == True:
            return
        
        print("Taking off...")
        self.client.takeoffAsync().join()
        self.client.moveToZAsync(self.INIT_POS.z_val - height, 1).join()

        self.flying = True
        self.action_list.append({
            "action": "takeoff",
            "params":  {"height": height}
        })
        
    def land(self):
        if self.flying == False:
            return
        
        print("Landing...")
        self.client.landAsync().join()
        self.action_list.append({
            "action": "land"
        })

    def cancel_action(self):
        self.client.cancelLastTask()
        
    def check_takeoff(self):
        if self.flying == False:
            print("Try to move drone without taking off, please wait until drone is up!")
            self.takeoff()
    
    # moving
    def move_forward(self, value):
        self.check_takeoff()
        
        print(f"Moving forward for {value}m at {(value/self.DUR):.2f}m/s...")
        self.client.moveByVelocityBodyFrameAsync(vx=(value/self.DUR), vy=0, vz=0, duration=self.DUR).join()
        self.action_list.append({
            "action": "move_forward",
            "params": {"distance": value}
        })
        
    def rotate_counter_clock(self, value):
        self.check_takeoff()
        
        print(f"Rotating counter clockwise for {value} degree at {self.ROTATE_SPEED}deg/s...")
        self.client.rotateToYawAsync(value, self.ROTATE_SPEED).join()
        self.action_list.append({
            "action": "rotate_counter_clock",
            "params": {"angle": value}
        })
    
    # getters
    def get_position(self):
        state = self.client.getMultirotorState()
        pos = state.kinematics_estimated.position
        # print(f"Position: X={pos.x_val:.2f}, Y={pos.y_val:.2f}, Z={pos.z_val:.2f}")
        return pos
        
    def cleanup(self):
        """Cleanup and disconnect drone"""
        print("Cleaning up...")
        if self.client is not None:
            self.client.armDisarm(False)
            self.client.enableApiControl(False)
            self.client.reset()