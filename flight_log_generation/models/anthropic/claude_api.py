import anthropic
from dotenv import load_dotenv
import os
import base64

load_dotenv()

client = anthropic.Anthropic(api_key = os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model = "claude-3-7-sonnet-20250219",
    max_tokens = 300,
    temperature = 1,
    system = "You are a world-class poet. Respond only with short poems.",
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Why is the ocean salty?"
                }
            ]
        }
    ]
)

print(message.content[0].text)