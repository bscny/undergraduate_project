# prompt for cloud models, outputs an JSON
prompt_json = """
You are analyzing an aerial image taken by a drone. For the given aerial image, perform the following structured observations:

1. Landmarks
   - landmark_name: Name or category of the landmark (e.g., "building", "bridge", "road", "forest patch", "communication tower", "farmland", etc.).
   - position: One of the following 8 options only — "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right", "middle".
   - visual_description: A detailed description of the landmark's appearance (include size, shape, color, texture, special characteristics like "red rooftop", "dense green foliage", "long, winding road", etc.).

2. Anomalies
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