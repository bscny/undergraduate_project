import anthropic
from dotenv import load_dotenv
from utils.image import image_processor
from utils import prompts
import os

# parse a given image to json files
def parse_images_json(image_path):
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    # Getting the Base64 string
    base64_image = image_processor.encode_image(image_path)
    
    message = client.messages.create(
        model = "claude-3-7-sonnet-20250219",
        max_tokens = 2000,
        temperature = 0,
        # system = "You are a world-class poet. Respond only with short poems.",
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompts.prompt_json
                    },
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": base64_image
                        }
                    }
                ]
            }
        ]
    )

    print(message.content[0].text)
    
# parse a given image batch to json files
def parse_image_batch_json(image_folder_path, start_index, end_index):
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    content = []
    
    content.append({
        "type": "text",
        "text": prompts.prompt_json_batch
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