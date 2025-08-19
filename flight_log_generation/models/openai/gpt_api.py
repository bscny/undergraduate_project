from dotenv import load_dotenv
from openai import OpenAI
from utils.image import image_processor
from utils.prompts import prompts_json
import os
    
# parse a given image to json files
def parse_images_json(image_path):
    load_dotenv()

    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

    # Getting the Base64 string
    base64_image = image_processor.encode_image(image_path)
    
    response = client.responses.create(
        model="gpt-4o",
        temperature = 0,
        max_output_tokens = 2000,
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": prompts_json.prompt_json },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                        "detail": "high"
                    },
                ],
            }
        ],
    )

    print(response.output_text)
    
# parse a given image batch to json files
def parse_image_batch_json(image_path):
    load_dotenv()

    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

    # Getting the Base64 string
    base64_image0 = image_processor.encode_image(image_path + "temp_0.jpg")
    base64_image1 = image_processor.encode_image(image_path + "temp_1.jpg")
    base64_image2 = image_processor.encode_image(image_path + "temp_2.jpg")
    
    response = client.responses.create(
        model="gpt-4o",
        temperature = 0,
        max_output_tokens = 2000,
        input=[
            {
                "role": "user",
                "content": [
                    { "type": "input_text", "text": prompts_json.prompt_json_batch },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image0}",
                        "detail": "high"
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image1}",
                        "detail": "high"
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{base64_image2}",
                        "detail": "high"
                    },
                ],
            }
        ],
    )

    print(response.output_text)
    
# parse a given image with wolf's pipeline
def parse_image(image_path, prompt, prev_desc = None):
    load_dotenv()

    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
    
    content = []
    
    content.append({
        "type": "input_text",
        "text": prompt
    })
    
    if prev_desc is not None:
        content.append({
            "type": "input_text",
            "text": "previous key frame's description: \n" + prev_desc
        })
        
    base64_image = image_processor.encode_image(f"{image_path}")
    
    content.append({
        "type": "input_image",
        "image_url": f"data:image/jpeg;base64,{base64_image}",
        "detail": "high",
    })
    
    response = client.responses.create(
        model="gpt-4o",
        temperature = 0.5,
        max_output_tokens = 2000,
        input=[
            {
                "role": "user",
                "content": content
            }
        ],
    )

    return response.output_text

def summarize(captions, instruction, prompt):
    load_dotenv()

    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
    
    content = []
    
    content.append({
        "type": "input_text",
        "text": prompt
    })
    
    content.append({
        "type": "input_text",
        "text": instruction
    })
    
    content.append({
        "type": "input_text",
        "text": captions
    })
    
    response = client.responses.create(
        model="gpt-4o",
        temperature = 0,
        max_output_tokens = 2000,
        input=[
            {
                "role": "user",
                "content": content
            }
        ],
    )
    
    return response.output_text

def merge_logs(log1, log2, prompt):
    load_dotenv()

    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
    
    content = []
    
    content.append({
        "type": "input_text",
        "text": prompt
    })
    
    content.append({
        "type": "input_text",
        "text": log1
    })
    
    content.append({
        "type": "input_text",
        "text": log2
    })
    
    response = client.responses.create(
        model="gpt-4o",
        temperature = 0,
        max_output_tokens = 2000,
        input=[
            {
                "role": "user",
                "content": content
            }
        ],
    )
    
    return response.output_text