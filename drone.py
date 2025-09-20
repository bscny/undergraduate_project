import airsim
from dotenv import load_dotenv
import os
import base64

load_dotenv()

class Drone:   
    def __init__(self):
        self.client = airsim.MultirotorClient(ip=os.getenv("WINDOWS_IP"))
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        self.client.simPrintLogMessage("Hello World~~")

        # define some constant here
        self.LINEAR_DUR = 3  # in seconds
        self.ANGULAR_DUR = 1  # in seconds
        self.SPEED = 7  # in m/s
        self.ROTATE_SPEED = 45  # in deg/s
        self.INIT_POS = self.get_position()  # this has x_val, y_val, z_val
        self.MAX_PAST_FRAMES = 4
        
        # define some private variables
        self.flying = False
        self.action_list = []  # lowest level
        self.navigation_list = []  # mid level
        self.altitude = self.INIT_POS.z_val  # record this to have consistent fly height
        self.frames_queue = []
        
    def set_posotion(self, x, y, z, yaw):
        pose = airsim.Pose(
            airsim.Vector3r(x, y, z),  # X, Y, Z in NED
            airsim.to_quaternion(0, 0, yaw)  # roll, pitch, yaw
        )

        self.client.simSetVehiclePose(pose=pose, ignore_collision=True)

    def cleanup(self):
        # for recording
        if self.client.isRecording():
            self.client.stopRecording()

        print("Cleaning up...")
        if self.client is not None:
            self.client.armDisarm(False)
            self.client.enableApiControl(False)
            self.client.reset()
            
    def take_picture(self):           
        # take pic
        base64_string = self.client.simGetImage("3", airsim.ImageType.Scene)
        try:
            decoded_bytes = base64.b64encode(base64_string).decode("utf-8")
        except Exception as e:
            print(f"Error encoding frames when taking picture: {e}")
            self.client.simPrintLogMessage(f"Error encoding frames when taking picture: {e}")
            self.cleanup()
            exit()

        if len(self.frames_queue) >= self.MAX_PAST_FRAMES:
            # Remove the oldest frame if queue is full
            self.frames_queue.pop(0)

        self.frames_queue.append(decoded_bytes)

    # BELOWS ARE MEMBER FUNCTIONS THAT CONTROL DRONE ACTIONS
    # basic actions
    def takeoff(self, height = 3):
        if height <= 0:
            print("can't fly under ground...")
            return
        
        if self.flying == True:
            return
        
        print("Taking off...")
        self.client.simPrintLogMessage("Taking off...")
        self.take_picture()
        self.client.takeoffAsync().join()
        self.client.moveToZAsync(self.INIT_POS.z_val - height, 1).join()
        
        self.altitude = self.INIT_POS.z_val - height
        self.flying = True
        self.action_list.append({
            "action": "takeoff",
            "params":  {"height": height}
        })
        
        # start recording if it's the first takeoff
        if not self.client.isRecording():
            self.client.startRecording()
        
    def land(self):
        if self.flying == False:
            return
        
        print("Landing...")
        self.take_picture()
        self.client.simPrintLogMessage("Landing...")
        self.client.moveToZAsync(self.INIT_POS.z_val - 3, 1).join()
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
        
        # print message out
        print(f"Moving forward {value}m at {self.SPEED}m/s for {(value/self.SPEED):.2f} seconds...")
        self.client.simPrintLogMessage(f"Moving forward {value}m at {self.SPEED}m/s for {(value/self.SPEED):.2f} seconds...")

        self.take_picture()
        self.client.moveByVelocityBodyFrameAsync(vx=self.SPEED, vy=0, vz=0, duration=value/self.SPEED).join()
        self.client.moveToZAsync(self.altitude, 1).join()  # keep consistent fly height
        self.action_list.append({
            "action": "move_forward",
            "params": {"distance": value}
        })
        
    def rotate(self, value):
        self.check_takeoff()
        
        # print message out
        print(f"Rotating {value} degree clockwise at {self.ROTATE_SPEED}deg/s for {(value/self.ROTATE_SPEED):.2f} seconds...")
        self.client.simPrintLogMessage(f"Rotating {value} degree clockwise at {self.ROTATE_SPEED}deg/s for {(value/self.ROTATE_SPEED):.2f} seconds...")

        offset = 1
        if value < 0:
            offset = -1
        
        self.take_picture()
        self.client.rotateByYawRateAsync(yaw_rate=self.ROTATE_SPEED * offset, duration=value * offset/self.ROTATE_SPEED).join()
        self.client.moveToZAsync(self.altitude, 1).join()  # keep consistent fly height
        self.action_list.append({
            "action": "rotate",
            "params": {"angle": value}
        })
    
    # getters
    def get_position(self):
        state = self.client.getMultirotorState()
        pos = state.kinematics_estimated.position
        # print(f"Position: X={pos.x_val:.2f}, Y={pos.y_val:.2f}, Z={pos.z_val:.2f}")
        return pos