from dotenv import load_dotenv
import base64
import os
from google import genai
from google.genai import types

load_dotenv()

def generate():
    client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))

    contents = [
#         types.Content(
#             role="user",
#             parts=[
#                 types.Part.from_text(text="""hello whats ur name"""),
#             ],
#         ),
#         types.Content(
#             role="model",
#             parts=[
#                 types.Part.from_text(text="""I am a large language model, trained by Google. I don't have a name.
# """),
#             ],
#         ),
#         types.Content(
#             role="user",
#             parts=[
#                 types.Part.from_text(text="""oh i thought ur name is Gemini"""),
#             ],
#         ),
#         types.Content(
#             role="model",
#             parts=[
#                 types.Part.from_text(text="""Gemini is the name of the large language model I'm based on. You can think of me as a version of Gemini.
# """),
#             ],
#         ),
        types.Content(
            role = "user",
            parts = [
                types.Part.from_text(text = """Write a one-sentence bedtime story about a unicorn."""),
            ],
        ),
    ]
    
    generate_content_config = types.GenerateContentConfig(
        temperature = 0,
        max_output_tokens = 300,
        response_mime_type = "text/plain",
    )
    
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = contents,
        config = generate_content_config
    )
    
    print(response.text)

if __name__ == "__main__":
    generate()
