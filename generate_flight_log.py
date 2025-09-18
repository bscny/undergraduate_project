import cv2
import os
import threading

# custom packages
from models.anthropic import claude_api
from models.openai import gpt_api
from models.google import gemini_api

from utils.prompts import frame_prompts
from utils.prompts import summary_prompts
from utils.prompts import log_gen_prompts

import input as inp

# define some constant here
# path
VIDEO_NAME = "simcity.mp4"  # the only thing that has to be changed!!
LOG_NAME = "TBD"
VIDEO_FOLDER_PATH = "assets/large_files/videos/"
IMAGE_FOLDER_PATH = "assets/large_files/image2parse/"
TEXT_FOLDER_PATH = "assets/flight_logs/"

# frame related
PARSE_INTERVAL = 3  # in seconds
IMAGE_BATCHES = 10
START_TIME = 0  # in seconds
MAX_WIDTH = 640
MAX_HEIGHT = 480

# Instruction
# INSTRUCTION = '''summarize this video, and especially state all the landmarks you see (list them according to the order of time).'''

def frame_by_frame_processing(pre_flight_info):
    # Clear the captions.txt file before starting
    with open(TEXT_FOLDER_PATH + LOG_NAME + "/captions.txt", "w", encoding="utf-8") as f:
        f.write("")

    cap = cv2.VideoCapture(VIDEO_FOLDER_PATH + VIDEO_NAME)
    
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    else:
        # start parsing the video at `START_TIME` second, omit the take off time
        # ps. always have to read() after set() so opencv don't forget the pin point position 
        cap.set(cv2.CAP_PROP_POS_MSEC, START_TIME * 1000)
        cap.read()
        
    # image_buffer_index = 0
    captions = []
    prompt = frame_prompts.prompt_wolf_less_structure

    while True:
        # Set the position in milliseconds
        current_time_ms = cap.get(cv2.CAP_PROP_POS_MSEC)
        
        ret, frame = cap.read()
        
        if not ret:
            print("reached final frame. Exiting ...")
            # in case that there are still frames in the batches
            # print(llava_api.parse_images(IMAGE_FOLDER_PATH, image_buffer_index))
            
            break
        
        print(f"Timestamp: {(current_time_ms / 1000):.2f} seconds")
        
        height, width = frame.shape[:2]
        scaling_factor = min(MAX_WIDTH / width, MAX_HEIGHT / height)
        # Resize only if larger than desired size
        if scaling_factor < 1:
            frame = cv2.resize(frame, (int(width * scaling_factor), int(height * scaling_factor)), interpolation=cv2.INTER_AREA)
        
        # cv2.imshow("frame", frame)
        
        # writes the frame to IMAGE_FOLDER_PATH
        cv2.imwrite(IMAGE_FOLDER_PATH + "image.jpg", frame)
        # cv2.imwrite(f"{IMAGE_FOLDER_PATH}temp_{image_buffer_index}.jpg", frame)
        
        # get captions from claude for each frame
        # for the 1st frame only:
        if len(captions) == 0:
            content = gpt_api.parse_image(IMAGE_FOLDER_PATH + "image.jpg", prompt)
        else:
            content = gpt_api.parse_image(IMAGE_FOLDER_PATH + "image.jpg", prompt, captions[-1])

        captions.append(content)
        
        # Skip the next frames by setting the video position
        cap.set(cv2.CAP_PROP_POS_MSEC, current_time_ms + (PARSE_INTERVAL * 1000))
        cap.read()
        
        # image_buffer_index += 1
        
        # if image_buffer_index == IMAGE_BATCHES:
        #     # start parsing the frame batch
        #     # print(llava_api.parse_images(IMAGE_FOLDER_PATH, IMAGE_BATCHES))
            
        #     image_buffer_index = 0
        
        if cv2.waitKey(1) == ord('q'):
            return
        
    # organize the content to a single file start with FRAME 1: ...
    all_captions = ""
    with open(TEXT_FOLDER_PATH + LOG_NAME + "/captions.txt", "w", encoding="utf-8") as f:
        for idx, caption in enumerate(captions, start=1):
            all_captions += f"FRAME {idx}:\n"
            all_captions += (caption.strip() + "\n\n")
        
        f.write(all_captions)
            
    # make flight log based on the captions
    with open(TEXT_FOLDER_PATH + LOG_NAME + "/log_claude.md", "w", encoding="utf-8") as f:
        log = claude_api.flight_log(all_captions, log_gen_prompts.cap_to_complex_log, pre_flight_info)
        
        f.write(log)
        
    cap.release()
    cv2.destroyAllWindows()
    os.remove(IMAGE_FOLDER_PATH + "image.jpg")
    
    print("Frame-by-frame processing completed!")
    
def gemini_video_processing(pre_flight_info):
    with open(TEXT_FOLDER_PATH + LOG_NAME + "/log_gemini.md", "w", encoding="utf-8") as f:
        log = gemini_api.parse_video(VIDEO_FOLDER_PATH + VIDEO_NAME, log_gen_prompts.video_to_complex_log, pre_flight_info)
        f.write(log)

    print("Gemini video processing completed!")
    
if __name__ == "__main__":
    LOG_NAME = input("Enter the log name: ").strip()
    
    # Create the end folder for this flight log
    if os.path.exists(TEXT_FOLDER_PATH + LOG_NAME):
        print("flight log generated already")
        exit()
    os.mkdir(TEXT_FOLDER_PATH + LOG_NAME)
    
    # Input the pre-flight information
    pre_flight_info = inp.input_drone_flight_log(VIDEO_FOLDER_PATH + VIDEO_NAME)

    # Create threads for both processes
    thread1 = threading.Thread(target=frame_by_frame_processing, args=(pre_flight_info,), name="FrameProcessor")
    thread2 = threading.Thread(target=gemini_video_processing, args=(pre_flight_info,), name="GeminiProcessor")
    
    print("Starting both video processing threads...")
    
    # Start both threads
    thread1.start()
    thread2.start()
    
    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    
    print("Both video processing tasks completed! Start generating merged log")
    
    with open(TEXT_FOLDER_PATH + LOG_NAME + "/log_claude.md", 'r') as f:
        log_frame_by_frame = f.read()
        
    with open(TEXT_FOLDER_PATH + LOG_NAME + "/log_gemini.md", 'r') as f:
        log_gemini = f.read()
        
    with open(TEXT_FOLDER_PATH + LOG_NAME + "/Flight_log.md", "w", encoding="utf-8") as f:
        final_log = claude_api.merge_logs(log_frame_by_frame, log_gemini, log_gen_prompts.merge_logs_prompt)
        f.write(final_log)