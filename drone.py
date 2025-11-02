import airsim
from dotenv import load_dotenv
import os

# custom package
from utils.image import image_processor
from output import drone_print

load_dotenv()

class Drone:   
    def __init__(self, custom_weather = False, record = False):
        self.client = airsim.MultirotorClient(ip=os.getenv("WINDOWS_IP"))
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        self.client.simPrintLogMessage("Hello World~~")
        self.temp = None
        # the weather API
        if custom_weather:
            self.client.simEnableWeather(True)
            self.client.simSetWeatherParameter(airsim.WeatherParameter.Rain, 1.0)
            self.client.simSetWeatherParameter(airsim.WeatherParameter.Fog, 0.02)
            self.client.simSetTimeOfDay(is_enabled=True, start_datetime="2024-10-13 23:30:00", is_start_datetime_dst=False, 
                                        celestial_clock_speed=1, update_interval_secs=60, move_sun=True)

        # define some constant here
        self.LINEAR_DUR = 3  # in seconds
        self.ANGULAR_DUR = 1  # in seconds
        self.SPEED = 7  # in m/s
        self.VERTICAL_SPEED = 3  # in m/s
        self.ROTATE_SPEED = 45  # in deg/s
        self.INIT_POS = self.get_position()  # this has x_val, y_val, z_val
        self.MAX_PAST_FRAMES = 4
        self.ORIG_WIDTH = 1920
        self.ORIG_HEIGHT = 1080
        self.RESIZE_WIDTH = 640
        self.RESIZE_HEIGHT = 360
        self.FOV_DEG = self.client.simGetCameraInfo("3").fov  # in deg
        self.RECORD = record
        
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
        if self.RECORD and self.client.isRecording():
            self.client.stopRecording()

        drone_print("Cleaning up...")
        if self.client is not None:
            self.client.armDisarm(False)
            self.client.enableApiControl(False)
            self.client.reset()
            
    def take_picture(self):
        # take pic
        bin_code = self.client.simGetImage("3", airsim.ImageType.Scene)
        try:
            decoded_base64_str = image_processor.resize_with_aspect_ratio(bin_code, self.RESIZE_WIDTH, self.RESIZE_HEIGHT)
        except Exception as e:
            drone_print(f"Error encoding frames when taking picture: {e}")
            self.client.simPrintLogMessage(f"Error encoding frames when taking picture: {e}")
            self.cleanup()
            exit()

        if len(self.frames_queue) >= self.MAX_PAST_FRAMES:
            # Remove the oldest frame if queue is full
            self.frames_queue.pop(0)

        self.frames_queue.append(decoded_base64_str)
        
        self.temp = bin_code

    # BELOWS ARE MEMBER FUNCTIONS THAT CONTROL DRONE ACTIONS
    # basic actions
    def takeoff(self, height = 30):
        if height <= 0:
            drone_print("can't fly under ground...")
            return
        
        if self.flying == True:
            return
        
        drone_print("Taking off...")
        self.client.simPrintLogMessage("Taking off...")
        self.client.takeoffAsync().join()
        self.client.moveToZAsync(self.INIT_POS.z_val - height, 10).join()
        self.client.moveToZAsync(self.INIT_POS.z_val - height, self.VERTICAL_SPEED).join()
        self.take_picture()
        
        self.altitude = self.INIT_POS.z_val - height
        self.flying = True
        self.action_list.append({
            "action": "takeoff",
            "params":  {"height": height}
        })
        
        # start recording if it's the first takeoff
        if self.RECORD and (not self.client.isRecording()):
            self.client.startRecording()
        
    def land(self):
        if self.flying == False:
            return
        
        drone_print("Landing...")
        self.client.simPrintLogMessage("Landing...")
        self.client.moveToZAsync(self.INIT_POS.z_val - 3, self.VERTICAL_SPEED).join()
        self.client.landAsync().join()
        self.take_picture()
        self.action_list.append({
            "action": "land"
        })

    def cancel_action(self):
        self.client.cancelLastTask()
        
    def check_takeoff(self):
        if self.flying == False:
            drone_print("Try to move drone without taking off, please wait until drone is up!")
            self.takeoff(-self.altitude)
    
    # moving
    def move_vertical(self, value):
        self.check_takeoff()
        
        offset = -1
        if value < 0:  # fly down
            offset = 1
        
        # print message out
        drone_print(f"Moving vertically {value:.2f}m at {self.VERTICAL_SPEED}m/s for {(abs(value)/self.VERTICAL_SPEED):.2f} seconds...")
        self.client.simPrintLogMessage(f"Moving vertically {value:.2f}m at {self.VERTICAL_SPEED}m/s for {(abs(value)/self.SPEED):.2f} seconds...")

        self.client.moveByVelocityBodyFrameAsync(vx=0, vy=0, vz=self.VERTICAL_SPEED * offset, duration=abs(value)/self.VERTICAL_SPEED).join()
        self.take_picture()
        self.altitude -= value
        self.action_list.append({
            "action": "move_vertical",
            "params": {"height": value}
        })

    def move_forward(self, value):
        self.check_takeoff()
        
        # print message out
        drone_print(f"Moving forward {value:.2f}m at {self.SPEED}m/s for {(value/self.SPEED):.2f} seconds...")
        self.client.simPrintLogMessage(f"Moving forward {value:.2f}m at {self.SPEED}m/s for {(value/self.SPEED):.2f} seconds...")

        self.client.moveByVelocityBodyFrameAsync(vx=self.SPEED, vy=0, vz=0, duration=value/self.SPEED).join()
        self.take_picture()
        self.client.moveToZAsync(self.altitude, self.VERTICAL_SPEED).join()  # keep consistent fly height
        self.action_list.append({
            "action": "move_forward",
            "params": {"distance": value}
        })
        
    def rotate(self, value):
        self.check_takeoff()
        
        offset = 1
        if value < 0:  # fly left
            offset = -1

        # print message out
        drone_print(f"Rotating {value:.2f} degree clockwise at {self.ROTATE_SPEED}deg/s for {(value * offset/self.ROTATE_SPEED):.2f} seconds...")
        self.client.simPrintLogMessage(f"Rotating {value:.2f} degree clockwise at {self.ROTATE_SPEED}deg/s for {(value * offset/self.ROTATE_SPEED):.2f} seconds...")

        self.client.rotateByYawRateAsync(yaw_rate=self.ROTATE_SPEED * offset, duration=value * offset/self.ROTATE_SPEED).join()
        self.client.moveToZAsync(self.altitude, self.VERTICAL_SPEED).join()  # keep consistent fly height
        self.take_picture()
        self.action_list.append({
            "action": "rotate",
            "params": {"angle": value}
        })
    
    # getters
    def get_position(self):
        state = self.client.getMultirotorState()
        pos = state.kinematics_estimated.position
        # drone_print(f"Position: X={pos.x_val:.2f}, Y={pos.y_val:.2f}, Z={pos.z_val:.2f}")
        return pos