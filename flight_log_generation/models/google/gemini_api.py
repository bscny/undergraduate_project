from dotenv import load_dotenv
import os
import time
from google import genai
from google.genai import types
from utils.image import image_processor
from utils.prompts import prompts_json

# parse a given image to json files
def parse_images_json(image_path):
    load_dotenv()
    
    client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
    
    # Getting the Base64 string
    base64_image = image_processor.encode_image(image_path)

    contents = [
        types.Content(
            role = "user",
            parts = [
                types.Part.from_bytes(
                    data=base64_image,
                    mime_type='image/jpeg',
                ),
                types.Part.from_text(text = prompts_json.prompt_json),
            ],
        ),
    ]
    
    generate_content_config = types.GenerateContentConfig(
        temperature = 0,
        max_output_tokens = 2000,
        response_mime_type = "text/plain",
    )
    
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = contents,
        config = generate_content_config
    )
    
    print(response.text)

# parse a given image batch to json files  
def parse_image_batch_json(image_path):
    load_dotenv()
    
    client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
    
    # Getting the Base64 string
    base64_image0 = image_processor.encode_image(image_path + "temp_0.jpg")
    base64_image1 = image_processor.encode_image(image_path + "temp_1.jpg")
    base64_image2 = image_processor.encode_image(image_path + "temp_2.jpg")

    contents = [
        types.Content(
            role = "user",
            parts = [
                types.Part.from_bytes(
                    data=base64_image0,
                    mime_type='image/jpeg',
                ),
                types.Part.from_bytes(
                    data=base64_image1,
                    mime_type='image/jpeg',
                ),
                types.Part.from_bytes(
                    data=base64_image2,
                    mime_type='image/jpeg',
                ),
                types.Part.from_text(text = prompts_json.prompt_json_batch),
            ],
        ),
    ]
    
    generate_content_config = types.GenerateContentConfig(
        temperature = 0,
        max_output_tokens = 2000,
        response_mime_type = "text/plain",
    )
    
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = contents,
        config = generate_content_config
    )
    
    print(response.text)
    
def parse_video(video_path, instruction_prompt):
    load_dotenv()
    
    client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
    
    # Upload the video file
    try:
        myfile = client.files.upload(file=video_path)
    except Exception as e:
        print(f"Error uploading file: {e}")
        exit()
        
    # Check whether the file is ready to be used.
    f = client.files.get(name=myfile.name)
    while f.state.name == "PROCESSING":
        time.sleep(1)
        f = client.files.get(name=myfile.name)

    if f.state.name == "FAILED":
        print(f"Error using the uploaded file: {myfile.name}")
        exit()
    
    myfile = client.files.get(name=myfile.name)

    # Construct the content using the file reference
    contents = [
        myfile,
        instruction_prompt
    ]
    
    generate_content_config = types.GenerateContentConfig(
        temperature = 0,
        max_output_tokens = 5000,
        response_mime_type = "text/plain",
    )
    
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = contents,
        config = generate_content_config
    )
    
    return response.text

def file_api_checker():
    load_dotenv()
    
    client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
    
    for f in client.files.list():
        print(' ', f.state.name, ' ', f.name)