import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import os

# custom packages
from models.llava import llava_api

# define some constant here
VIDEO_PATH = "assets/large_files/videos"
PARSE_INTERVAL = 5  # in seconds

if __name__ == "__main__":
    cap = cv2.VideoCapture(VIDEO_PATH + "/city.MP4")
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
        
    # Get the video frame rate (fps)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(PARSE_INTERVAL * fps)

    while True:
        # Set the position in milliseconds
        current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
        print(f"Timestamp: {current_time_ms / 1000:.2f} seconds")

        # Skip the next frames by setting the video position
        cap.set(cv2.CAP_PROP_POS_MSEC, current_time_ms + (PARSE_INTERVAL * 1000))
        
        ret, frame = cap.read()
        
        if not ret:
            print("Can't receive frame. Exiting ...")
            break
        
        cv2.imshow("frame", frame)
        
        if current_time_ms / 1000 < 62 and current_time_ms / 1000 > 58:
            cv2.imwrite("temp.jpg", frame)
            print(llava_api.parse_given_image("temp.jpg"))
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    os.remove("temp.jpg")