import base64
import cv2
import os
from natsort import natsorted
import io
from PIL import Image

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
    
# from binary image code to a resized base64 string
def resize_with_aspect_ratio(binary_code, target_width, target_height, maintain_aspect=True) -> str:   
    image = Image.open(io.BytesIO(binary_code))
    
    # print(f"Original size: {image.size}")
    
    if maintain_aspect:
        # Calculate aspect ratio preserving dimensions
        original_ratio = image.width / image.height
        target_ratio = target_width / target_height
        
        if original_ratio > target_ratio:
            # Image is wider than target ratio
            new_width = target_width
            new_height = int(target_width / original_ratio)
        else:
            # Image is taller than target ratio
            new_width = int(target_height * original_ratio)
            new_height = target_height
        
        # print(f"Aspect ratio preserved size: {new_width}x{new_height}")
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    else:
        # Stretch to exact dimensions
        resized_image = image.resize((target_width, target_height), Image.Resampling.LANCZOS)
        print(f"Stretched to: {target_width}x{target_height}")
    
    # Convert back to base64
    buffer = io.BytesIO()
    format = image.format if image.format else 'JPEG'
    resized_image.save(buffer, format=format, quality=85)
    resized_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return resized_base64