import anthropic
from dotenv import load_dotenv
from utils.image import image_processor
import os
import json

# parse a given image to json files
def parse_images(image_path, prompt, prev_desc = None):
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    content = []
    
    content.append({
        "type": "text",
        "text": prompt
    })
    
    if prev_desc is not None:
        content.append({
            "type": "text",
            "text": "previous key frame's description: \n" + prev_desc
        })
    
    # Getting the Base64 string
    base64_image = image_processor.encode_image(image_path)
    
    content.append({
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/jpeg",
            "data": image_processor.encode_image(f"{image_path}")
        }
    })
    
    message = client.messages.create(
        model = "claude-3-7-sonnet-20250219",
        max_tokens = 2000,
        temperature = 0,
        # system = "You are a world-class poet. Respond only with short poems.",
        messages = [
            {
                "role": "user",
                "content": content
            }
        ]
    )

    return message.content[0].text
    
# parse a given image batch to json files
def parse_image_batch_json(image_folder_path, start_index, end_index, prompt, prev_json = None, prev_frame = None):
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    content = []
    
    content.append({
        "type": "text",
        "text": prompt
    })
    
    if prev_json is not None:
        content.append({
            "type": "text",
            "text": "previous frame's metadata: " + json.dumps(prev_json)
        })
        
        content.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": prev_frame
            }
        })
    
    for i in range(start_index, end_index + 1):
        content.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/jpeg",
                "data": image_processor.encode_image(f"{image_folder_path}temp_{i}.jpg")
            }
        })
    
    message = client.messages.create(
        model = "claude-3-7-sonnet-20250219",
        max_tokens = 5000,
        temperature = 0,
        # system = "You are a world-class poet. Respond only with short poems.",
        messages = [
            {
                "role": "user",
                "content": content
            }
        ]
    )

    print(message.content[0].text)