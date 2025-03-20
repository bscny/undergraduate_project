import cv2
import os

# custom packages
from models.llava import llava_api

# define some constant here
VIDEO_PATH = "assets/large_files/videos/"
# IMAGE_PATH = "assets/large_files/image2parse/"
IMAGE_PATH = "assets/test_images/"
PARSE_INTERVAL = 5  # in seconds
IMAGE_BATCHES = 10

if __name__ == "__main__":
    cap = cv2.VideoCapture(VIDEO_PATH + "city.MP4")
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()
    else:
        # start parsing the video at 40 second, omit the take off time
        cap.set(cv2.CAP_PROP_POS_MSEC, (40 - PARSE_INTERVAL) * 1000)
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
            
            print(llava_api.parse_given_images(IMAGE_PATH, image_buffer_index))
            
            break
        
        print(f"Timestamp: {(current_time_ms + (PARSE_INTERVAL * 1000)) / 1000:.2f} seconds")
        cv2.imshow("frame", frame)
        
        cv2.imwrite(f"{IMAGE_PATH}temp_{image_buffer_index}.jpg", frame)
        
        image_buffer_index += 1
        
        if image_buffer_index == IMAGE_BATCHES:
            # start parsing
            print(llava_api.parse_given_images(IMAGE_PATH, IMAGE_BATCHES))
            
            image_buffer_index = 0
            break
        
        if cv2.waitKey(1) == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
    # os.remove("temp.jpg")