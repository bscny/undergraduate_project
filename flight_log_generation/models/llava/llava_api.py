import ollama
import json

def describe_image(image_path):
    prompt = """
    Describe the image from my drone as detailed as possible. Follow this structured format for clarity and completeness:
    
    General Overview:Begin with a brief summary of the scene, identifying the primary environment (e.g., residential area, industrial zone, park, etc.) and key visual features.

    Detailed Observations:Provide a numbered list describing notable details in the image. Each point should include:

    - Clear identification of objects or landmarks.
    - Relative positioning (e.g., "to the left of...", "in the background...", "near the center...").
    - Descriptions of condition, appearance, or notable characteristics (e.g., "well-maintained", "damaged", "overgrown", etc.).
    """
    
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
    prompt = """
    "Analyze the given image from a drone camera and provide detailed observations in a valid JSON data type (not as a string or markdown). 

    Include the following details: 

    1. Landmarks and Environment Features:  
    - Identify key landmarks (e.g., buildings, mountains, rivers, etc.).  
    - Provide their approximate positions in the image (e.g., top-left, center, bottom-right).  
    - Use descriptive adjectives to detail visual features (e.g., 'tall red tower', 'dense green forest').  

    2. Special Events and Anomalies:  
    - Highlight any unusual activities, movements, or visual anomalies (e.g., 'smoke rising', 'crowd gathering', 'damaged structure').  

    3. Weather Conditions:  
    - Describe visible weather conditions (e.g., 'clear sky', 'foggy horizon', 'heavy rain').  
    - Include details on visibility (e.g., 'excellent', 'limited due to haze', 'poor visibility from mist').
    
    "Format your response in an JSON data type:
    ```json
    {
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
    }
    ```

    Format your response as a valid JSON data type."
    """
    
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

    content = res['message']['content'].strip().strip('`').strip('JSON').strip('python').strip('json')
    
    return content

    try:
        result = json.loads(content)
    except json.JSONDecodeError:
        print("Failed to decode response as JSON.")
    
    return result

def parse_images(image_path, n):
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
