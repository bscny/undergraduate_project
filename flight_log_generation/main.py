import cv2
import os

# custom packages
from utils.prompts import prompts

# define some constant here
# path
VIDEO_FOLDER_PATH = "assets/large_files/videos/"
IMAGE_FOLDER_PATH = "assets/large_files/images/"

# frame related
PARSE_INTERVAL = 3  # in seconds
IMAGE_BATCHES = 10
START_TIME = 40  # in seconds
MAX_WIDTH = 640
MAX_HEIGHT = 480

if __name__ == "__main__":
    cap = cv2.VideoCapture(VIDEO_FOLDER_PATH + "city.MP4")
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
    else:
        # start parsing the video at `START_TIME` second, omit the take off time
        cap.set(cv2.CAP_PROP_POS_MSEC, (START_TIME - PARSE_INTERVAL) * 1000)
        cap.read()
        
    image_buffer_index = 0

    while True:
        # Set the position in milliseconds
        current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)

        # Skip the next frames by setting the video position
        cap.set(cv2.CAP_PROP_POS_MSEC, current_time_ms + (PARSE_INTERVAL * 1000))
        
        ret, frame = cap.read()
        
        if not ret:
            print("Can't receive frame. Exiting ...")
            # print(llava_api.parse_images(IMAGE_FOLDER_PATH, image_buffer_index))
            
            break
        
        print(f"Timestamp: {(current_time_ms + (PARSE_INTERVAL * 1000)) / 1000:.2f} seconds")
        
        height, width = frame.shape[:2]
        scaling_factor = min(MAX_WIDTH / width, MAX_HEIGHT / height)
        # Resize only if larger than desired size
        if scaling_factor < 1:
            frame = cv2.resize(frame, (int(width * scaling_factor), int(height * scaling_factor)), interpolation=cv2.INTER_AREA)
        
        cv2.imshow("frame", frame)
        
        # writes the frame to IMAGE_FOLDER_PATH with name of temp_{image_buffer_index}.jpg
        cv2.imwrite(f"{IMAGE_FOLDER_PATH}temp_{image_buffer_index}.jpg", frame)
        
        image_buffer_index += 1
        
        if image_buffer_index == IMAGE_BATCHES:
            # start parsing the frame batch
            # print(llava_api.parse_images(IMAGE_FOLDER_PATH, IMAGE_BATCHES))
            
            image_buffer_index = 0
            
            # test purpose
            break
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    # os.remove("temp.jpg")