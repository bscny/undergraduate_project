from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
from utils.image import image_processor
from utils import prompts

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
                types.Part.from_text(text = prompts.prompt_json),
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