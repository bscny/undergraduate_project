import ollama
import json

def describe_image(image_path):
    prompt = "Describe the image from my drone as detailed as possible"
    
    res = ollama.chat(
        model="llava:13b",
        messages=[
            {
                'role': 'user',
                'content': prompt,
                'images': [image_path]
            }
        ]
    )

    content = res['message']['content'].strip().strip('python').strip('`').strip('JSON').strip('json')
    
    return content

def parse_image_json(image_path):
    res = ollama.chat(
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
                'images': [image_path]
            }
        ]
    )

    content = res['message']['content'].strip().strip('`').strip('JSON').strip('python')
    
    # return content

    try:
        result = json.loads(content)
    except json.JSONDecodeError:
        print("Failed to decode response as JSON.")
    
    return result

def parse_given_images(image_path, n):
    images = []
    for i in range(0, n):
        images.append(f"{image_path}temp_{i}.jpg")

    prompt_json = """
    You are an advanced visual observer analyzing images from a drone camera. The images are extracted from a drone video at **5-second intervals**, meaning each image is sampled every 5 seconds. For each image provided, generate a JSON block that describes the following details:

    1. **Landmarks and Environment Features**
       - Identify prominent landmarks, natural or man-made (e.g., buildings, trees, roads).
       - Include positional details (e.g., "center-left", "top-right", etc.) and relevant adjectives describing size, color, or state (e.g., "tall red tower", "dense green forest").

    2. **Special Events and Anomalies**
       - Describe unusual occurrences (e.g., fire, smoke, crowd gathering) with relevant positioning and estimated scale.

    3. **Weather Conditions**
       - Describe visibility conditions (e.g., "clear sky", "foggy with reduced visibility").
       - Include details like lighting conditions and notable weather patterns.

    4. **Connections Between Images**
       - Identify temporal or spatial links between the current and previous images (e.g., "same vehicle moved 10m ahead", "clouds thickened").
       - Since images are taken at 5-second intervals, describe movement, progression, or changes accordingly.

    **Output Format:**
    ```json
    [
      {
        "image_id": "<image_1_id>",
        "landmarks": [
          {"name": "<landmark_name>", "position": "<relative_position>", "description": "<adjectives>"}
        ],
        "anomalies": [
          {"type": "<event_type>", "position": "<relative_position>", "description": "<adjectives or details>"}
        ],
        "weather": {
          "visibility": "<description>",
          "conditions": "<weather_details>"
        },
        "connections": {
          "space_relation": "<space_description>",
          "instance_relation": "<tracked_object_or_event>"
        }
      }
    ]
    ```

    **Additional Notes:**
    - If any category has no information, return an empty array or `null` for that field.
    - Since images are sampled every 5 seconds, ensure descriptions consider possible motion, changes in weather, and evolving anomalies over this interval.
    """
    
    prompt_text = """
    You are an advanced visual observer analyzing images from a drone camera. For each image provided, describe the visual content in as much detail as possible, organized by image number.
    Focus on observing and describing:
    - Landmarks and environment features, including their positions, shapes, colors, and any distinguishing details.
    - Any notable activities, events, or anomalies that stand out.
    - Weather conditions and visibility aspects as they appear in the image.

    Be precise and descriptive in your observations. Avoid summarizing or interpreting beyond what is visually evident. Your goal is to capture everything an attentive observer would notice in detail.
    Because it's important, let me emphasize it again, DO NOT summarize! DO NOT summarize! DO NOT summarize!
    
    Use the following format:

    image 1:
    [Detailed observations...]

    image 2:
    [Detailed observations...]
    
    image 3:
    [Detailed observations...]

    .....
    """
    
    prompt = "Describe these three images, they are images from my drone, and the interval is 3 seconds. Make sure the description is related to the timeline"

    res = ollama.chat(
        model="llava:13b",
        messages=[
            {
                'role': 'user',
                'content': prompt_text,
                # 'images': ['assets/large_files/image2parse/temp_0.jpg', 'assets/large_files/image2parse/temp_1.jpg', 'assets/large_files/image2parse/temp_2.jpg']
                'images': images
            }
        ]
    )

    content = res['message']['content'].strip().strip('python').strip('`').strip('JSON').strip('json')

    # try:
    #     result = json.loads(content)
    # except json.JSONDecodeError:
    #     print("Failed to decode response as JSON.")

    return content
