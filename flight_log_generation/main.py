import ollama
import numpy as np
import json

'''res = ollama.chat(
    model="llava:13b",
    messages=[
        {
            'role': 'user',
            'content': (
                "Analyze the given image from a drone camera and provide detailed observations in an python object data type (don't use markdown). "
                "Include the following details:\n\n"
                "1. **Landmarks and Environment Features:**\n"
                "   - Identify key landmarks (e.g., buildings, mountains, rivers, etc.).\n"
                "   - Provide their approximate positions in the image (e.g., top-left, center, bottom-right).\n"
                "   - Use descriptive adjectives to detail visual features (e.g., 'tall red tower', 'dense green forest').\n\n"
                "2. **Special Events and Anomalies:**\n"
                "   - Highlight any unusual activities, movements, or visual anomalies (e.g., 'smoke rising', 'crowd gathering', 'damaged structure').\n\n"
                "3. **Weather Conditions:**\n"
                "   - Describe visible weather conditions (e.g., 'clear sky', 'foggy horizon', 'heavy rain').\n"
                "   - Include details on visibility (e.g., 'excellent', 'limited due to haze', 'poor visibility from mist').\n\n"
                "Format your response in an python object data type (don't use markdown):\n\n"
                "{\n"
                "  \"landmarks\": [\n"
                "    {\n"
                "      \"name\": \"Mountain Peak\",\n"
                "      \"position\": \"top-center\",\n"
                "      \"description\": \"snow-covered with rocky outcrops\"\n"
                "    }\n"
                "  ],\n"
                "  \"events_anomalies\": [\n"
                "    {\n"
                "      \"type\": \"smoke\",\n"
                "      \"position\": \"bottom-left\",\n"
                "      \"description\": \"thick black smoke rising from a building\"\n"
                "    }\n"
                "  ],\n"
                "  \"weather\": {\n"
                "    \"condition\": \"partly cloudy\",\n"
                "    \"visibility\": \"moderate\"\n"
                "  }\n"
                "}"
            ),
            'images': ['./city-1.png', './city-2.png', './city-3.png']
        }
    ]
)'''

res = ollama.chat(
    model="llava:13b",
    messages=[
        {
            'role': 'user',
            'content': 'Describe these three images, they are images from my drone, and the interval is 3 seconds. Make sure the description is related to the timeline',
            'images': ['./city-1.png', './city-2.png', './city-3.png']
        }
    ]
)

print(res['message']['content'])

# content = res['message']['content'].strip().strip('```python').strip('```').strip('```JSON')

# try:
#     result = json.loads(content)
#     print(result['weather'])
# except json.JSONDecodeError:
#     print("Failed to decode response as JSON.")
