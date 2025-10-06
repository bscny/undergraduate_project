import anthropic
from dotenv import load_dotenv
from utils.image import image_processor
import os
import json

def hi():
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    content = []
    
    content.append({
        "type": "text",
        "text": "hello"
    })
    
    message = client.messages.create(
        model = "claude-sonnet-4-20250514",
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

# FLIGHT LOG GENERATING RELATED--------------------------------------------------------------------------------
# parse a given image with wolf's pipeline
def parse_image(image_path, prompt, prev_desc = None):
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
    
def summarize(captions, instruction, prompt):
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    content = []
    
    content.append({
        "type": "text",
        "text": prompt
    })
    
    content.append({
        "type": "text",
        "text": instruction
    })
    
    content.append({
        "type": "text",
        "text": captions
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

    return message.content[0].text

def flight_log(main_info, prompt, additional_info):
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    content = []
    
    content.append({
        "type": "text",
        "text": prompt
    })
    
    content.append({
        "type": "text",
        "text": additional_info
    })
    
    content.append({
        "type": "text",
        "text": main_info
    })
    
    message = client.messages.create(
        model = "claude-sonnet-4-20250514",
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

    return message.content[0].text

def merge_logs(log1, log2, prompt):
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    content = []
    
    content.append({
        "type": "text",
        "text": prompt
    })
    
    content.append({
        "type": "text",
        "text": log1
    })
    
    content.append({
        "type": "text",
        "text": log2
    })
    
    message = client.messages.create(
        model = "claude-sonnet-4-20250514",
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

    return message.content[0].text

# AUTO PILOT RELATED RELATED--------------------------------------------------------------------------------
def test(prompt, image):
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    content = []
    
    content.append({
        "type": "text",
        "text": prompt
    })
    
    content.append({
        "type": "image",
        "source": {
            "type": "base64",
            "media_type": "image/png",
            "data": image
        }
    })
    
    message = client.messages.create(
        model = "claude-sonnet-4-20250514",
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
    
def instruction_filter(instruction, prompt) -> str:
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    content = []
    
    content.append({
        "type": "text",
        "text": prompt
    })
    
    content.append({
        "type": "text",
        "text": "User instruction:" + instruction
    })
    
    message = client.messages.create(
        model = "claude-sonnet-4-20250514",
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

    raw_text = message.content[0].text.strip("`")

    return raw_text
    
def decision_making(instruction, prompt, past_navigations, frames_queue) -> str:
    load_dotenv()

    client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))
    
    content = []
    
    content.append({
        "type": "text",
        "text": prompt
    })
    
    content.append({
        "type": "text",
        "text": "Past instructions (from old to new):\n" + past_navigations
    })
    
    content.append({
        "type": "text",
        "text": "Frames (from old to new): \n"
    })
    
    for frame in frames_queue:
        content.append({
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": "image/png",
                "data": frame
            }
        })
    
    content.append({
        "type": "text",
        "text": "User instruction:" + instruction
    })
    
    message = client.messages.create(
        model = "claude-sonnet-4-20250514",
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

    raw_text = message.content[0].text.strip("`")

    return raw_text