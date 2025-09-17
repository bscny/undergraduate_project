import base64
import cv2
import os
from natsort import natsorted

# Function to encode the image
def encode_image(image_path):   
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    except Exception as e:
        print(f"Error encoding file: {e}")
        exit()

def create_video_opencv(folder_path, output_path, fps=30):
    # Get all PNG files in the folder
    png_files = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            png_files.append(os.path.join(folder_path, filename))
    
    # Sort files naturally (important for timestamp-based names)
    png_files = natsorted(png_files)
    
    if not png_files:
        print(f"No PNG files found in {folder_path}!")
        return
    
    print(f"Found {len(png_files)} PNG files")
    
    # Read first image to get dimensions
    first_img = cv2.imread(png_files[0])
    if first_img is None:
        print(f"Could not read first image: {png_files[0]}")
        return
        
    height, width, layers = first_img.shape
    
    # Define codec and create VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # or use 'avc1' for better quality
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    print(f"Processing {len(png_files)} frames...")
    for i, file_path in enumerate(png_files):
        img = cv2.imread(file_path)
        if img is not None:
            video.write(img)
        else:
            print(f"Warning: Could not read {file_path}")
        
        if (i + 1) % 50 == 0:  # Progress indicator every 50 frames
            print(f"Processed {i + 1}/{len(png_files)} frames")
    
    video.release()
    cv2.destroyAllWindows()  # Clean up
    print(f"Video saved as {output_path}")