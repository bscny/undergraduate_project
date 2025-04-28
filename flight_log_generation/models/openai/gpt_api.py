from dotenv import load_dotenv
from openai import OpenAI
from utils.image import image_processor
from utils import prompts
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
                    { "type": "input_text", "text": prompts.prompt_json },
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