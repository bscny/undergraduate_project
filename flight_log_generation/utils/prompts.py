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
   - landmark_name: Name or category of the landmark (e.g., "building", "bridge", "road", "forest patch", "communication tower", "farmland", etc.), if repeated one already exists, give index.
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

- **movement_direction**: One of the following 9 directions — "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right", "stay".
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
      "frame_pair": [1, 2],
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

prompt_json_batchP1 = """
You are analyzing a sequence of aerial images taken by a drone. For the current batch of n aerial images (captured at 3-second intervals), perform the following structured observations for each frame **and** provide motion and identity inference across time.

INPUT FORMAT:

- You are provided with:
  1. A JSON object describing the **previous frame's metadata** under `previous_frame`, including:
     - frame_id (integer)
     - landmarks: list of landmarks (with name, position, and visual_description)
     - anomalies: list of anomalies (optional; same structure)
     - visibility: { weather, background_scene }
  2. A sequence of **n+1 images**:
     - The **first image** corresponds to the `previous_frame_image` (used only for continuity).
     - The next **n images** are the current batch of aerial frames: frame_1, frame_2, ..., frame_n.

YOUR TASK:

1. Per-Frame Observations (for the current n frames only)

For each frame `frame_i` (starting from 1), provide:

**Landmarks**
- landmark_name: A category or name (e.g., "building", "bridge", etc.). If similar to a landmark in `previous_frame`, reuse the name and append index (e.g., "building_2").
- position: One of — "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right", "middle".
- visual_description: Detailed description (size, color, texture, notable features).

**Anomalies** (only if present)
- anomaly_name: Category name (e.g., "fire", "flooded area", etc.). Reuse name from `previous_frame` if consistent.
- position: Same as above.
- visual_description: Detailed appearance (damage, shape, smoke, water, etc.).

**Visibility**
- weather: One of — "sunny", "cloudy", "foggy", "snowy", "rainy".
- background_scene: One of — "city", "desert", "forest", "ocean, lake, river", "agricultural area", "industrial area".

2. Motion Estimation

Estimate movement of the drone between:
- `previous_frame_image` and `frame_1`
- `frame_1` and `frame_2`, ..., `frame_{n-1}` and `frame_n`

Each movement should be one of — "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right", "stay"

3. Cross-Frame Identity Inference

Compare landmarks and anomalies across:
- `previous_frame` and `frame_1`
- all adjacent frames within the batch

For each matched object across frames:
- type: "landmark" or "anomaly"
- name: The assigned name (e.g., "building_2")
- frame_pair: [source_frame_id, target_frame_id]
- inference_probability: float from 0.0 to 1.0

---

OUTPUT FORMAT:

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
      "frame_pair": [1, 2],
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