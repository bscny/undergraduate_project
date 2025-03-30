from dotenv import load_dotenv
from openai import OpenAI
import os
import base64

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model = "gpt-4o",
    max_output_tokens = 300,
    temperature = 0,
    input = "Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)