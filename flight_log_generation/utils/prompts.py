# prompt for cloud models, outputs an JSON
prompt_json = """
You are analyzing an aerial image taken by a drone. For the given aerial image, perform the following structured observations:

1. Landmarks
   - landmark_name: Name or category of the landmark (e.g., "building", "bridge", "road", "forest patch", "communication tower", "farmland", etc.).
   - position: One of the following 8 options only — "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right", "middle".
   - visual_description: A detailed description of the landmark's appearance (include size, shape, color, texture, special characteristics like "red rooftop", "dense green foliage", "long, winding road", etc.).

2. Anomalies(if no obvious ones, do not list any)
   - anomaly_name: Name or category of the anomaly (e.g., "damaged building", "flooded area", "fire", "collapsed bridge", "traffic congestion", "illegal construction", etc.).
   - position: One of the following 8 options only — "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right", "middle".
   - visual_description: A detailed description of the anomaly's appearance (include extent of damage, color changes, irregular shapes, smoke, debris, water level, etc.).

3. Visibility
   - weather: Only select one from — "sunny", "cloudy", "foggy", "snowy", "rainy".
   - background_scene: Only select one from — "city", "desert", "forest", "ocean, lake, river", "agricultural area", "industrial area".

Return your answer strictly as a JSON object formatted like this:

Example JSON:

```json
{
  "landmarks": [
    {
      "landmark_name": "bridge",
      "position": "top-right",
      "visual_description": "A long suspension bridge with white cables spanning across a wide river, with noticeable shadow patterns on the water surface."
    },
    {
      "landmark_name": "industrial building",
      "position": "middle",
      "visual_description": "A large rectangular structure with a gray metallic roof and several ventilation units, surrounded by paved loading areas."
    }
  ],
  "anomalies": [
    {
      "anomaly_name": "flooded area",
      "position": "bottom-left",
      "visual_description": "Partially submerged farmland with patches of muddy water and scattered debris visible across the fields."
    }
  ],
  "visibility": {
    "weather": "cloudy",
    "background_scene": "agricultural area"
  }
}
```

Be thorough and detailed in the descriptions but stay strictly within the allowed choices for **position**, **weather**, and **background scene**."""

prompt_json_batch = """
You are analyzing a sequence of aerial images taken by a drone. For the given sequence of n aerial images, captured at 3-second intervals, perform the following structured observations for each frame **and** provide motion and identity inference across time:

1. Per-Frame Observations

Be as detailed as possible, report everything you see. For each frame `frame_i`, perform:

1. Landmarks
   - landmark_name: Name or category of the landmark (e.g., "building", "bridge", "road", "forest patch", "communication tower", "farmland", etc.).
   - position: One of the following 8 options only — "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right", "middle".
   - visual_description: A detailed description of the landmark's appearance (include size, shape, color, texture, special characteristics like "red rooftop", "dense green foliage", "long, winding road", etc.).

2. Anomalies(if no obvious ones, do not list any)
   - anomaly_name: Name or category of the anomaly (e.g., "damaged building", "flooded area", "fire", "collapsed bridge", "traffic congestion", "illegal construction", etc.).
   - position: One of the following 8 options only — "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right", "middle".
   - visual_description: A detailed description of the anomaly's appearance (include extent of damage, color changes, irregular shapes, smoke, debris, water level, etc.).

3. Visibility
   - weather: Only select one from — "sunny", "cloudy", "foggy", "snowy", "rainy".
   - background_scene: Only select one from — "city", "desert", "forest", "ocean, lake, river", "agricultural area", "industrial area".

2. Motion Between Frames

For each consecutive pair of frames (`frame_i` and `frame_{i+1}`), determine:

- **movement_direction**: One of the following 8 directions — "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right".
- This represents the general movement of the camera/drone between the two frames.

3. Cross-Frame Identity Inference

Attempt to track landmarks and anomalies across time. For any landmark or anomaly that appears in multiple frames:

- Assign a consistent **landmark_name** or **anomaly_name** where appropriate.
- Include a field `inference_probability` (from 0.0 to 1.0) to indicate confidence that the landmark or anomaly in `frame_i` and `frame_{i+1}` is the same.

Return your answer strictly as a JSON object formatted like this:

```json
{
  "frames": [
    {
      "frame_id": 1,
      "landmarks": [
        {
          "landmark_name": "bridge",
          "position": "top-right",
          "visual_description": "A long suspension bridge with white cables spanning a wide river."
        }
      ],
      "anomalies": [
        {
          "anomaly_name": "flooded area",
          "position": "bottom-left",
          "visual_description": "Farmland partially submerged in muddy water with debris."
        }
      ],
      "visibility": {
        "weather": "cloudy",
        "background_scene": "agricultural area"
      }
    },
    {
      "frame_id": 2,
      "landmarks": [
        {
          "landmark_name": "bridge",
          "position": "middle",
          "visual_description": "Same suspension bridge, now more centered in frame."
        }
      ],
      "anomalies": [
        {
          "anomaly_name": "flooded area",
          "position": "bottom",
          "visual_description": "Submerged area appears slightly extended toward the center."
        }
      ],
      "visibility": {
        "weather": "cloudy",
        "background_scene": "agricultural area"
      }
    }
  ],
  "motion": [
    {
      "from_frame": 1,
      "to_frame": 2,
      "movement_direction": "bottom-right"
    }
  ],
  "inference": [
    {
      "type": "landmark",
      "name": "bridge",
      "frame_pair": [1, 2],
      "inference_probability": 0.97
    },
    {
      "type": "anomaly",
      "name": "flooded area",
      "frame_pair": [1, 2],
      "inference_probability": 0.92
    }
  ]
}
```
"""