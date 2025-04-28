<details>
<summary>2025-04-28, test 3 cloud models to see how they handle JSON outputs (no timeline involved)</summary>

<details>
<summary>ChatGPT</summary>

# ChatGTP

```json
{
  "landmarks": [
    {
      "landmark_name": "basketball court",
      "position": "middle",
      "visual_description": "A rectangular basketball court with faded green and red paint, surrounded by a blue border. The court has two basketball hoops and is partially shaded by nearby trees."
    },
    {
      "landmark_name": "road",
      "position": "right",
      "visual_description": "A wide, multi-lane road with several parked cars along the side. The road has clear white lane markings and is bordered by a sidewalk with trees."
    },
    {
      "landmark_name": "building",
      "position": "top-left",
      "visual_description": "A building with a red-tiled roof and surrounding greenery, including dense trees and a small garden area."
    }
  ],
  "anomalies": [],
  "visibility": {
    "weather": "sunny",
    "background_scene": "city"
  }
}
```

```json
{
  "landmarks": [
    {
      "landmark_name": "temple",
      "position": "middle",
      "visual_description": "A traditional temple with ornate orange rooftops and intricate architectural details, surrounded by a courtyard with trees and pathways."
    },
    {
      "landmark_name": "parking lot",
      "position": "top-left",
      "visual_description": "A large parking area with multiple rows of parked cars, featuring a red paved surface and lined with trees."
    },
    {
      "landmark_name": "road",
      "position": "right",
      "visual_description": "A wide, multi-lane road with clear white lane markings, running parallel to the parking lot and bordered by trees."
    }
  ],
  "anomalies": [],
  "visibility": {
    "weather": "sunny",
    "background_scene": "city"
  }
}
```

```json
{
  "landmarks": [
    {
      "landmark_name": "parking lot",
      "position": "left",
      "visual_description": "A large parking lot filled with rows of parked cars, mostly white and silver, with a red paved surface and surrounded by trees."
    },
    {
      "landmark_name": "road",
      "position": "top",
      "visual_description": "A wide road with multiple lanes, marked with white lines and a pedestrian crossing, bordered by trees and sidewalks."
    },
    {
      "landmark_name": "building",
      "position": "bottom-right",
      "visual_description": "A building with a red rooftop and ornate architectural details, adjacent to a concrete area."
    }
  ],
  "anomalies": [],
  "visibility": {
    "weather": "sunny",
    "background_scene": "city"
  }
}
```
</details>

<details>
<summary>Claude</summary>

# Claude

```json
{
  "landmarks": [
    {
      "landmark_name": "basketball court",
      "position": "middle",
      "visual_description": "A green and blue multi-purpose sports court with white line markings for basketball. The court has a distinctive blue perimeter and green playing surface with visible basketball hoops."
    },
    {
      "landmark_name": "road",
      "position": "right",
      "visual_description": "A wide multi-lane asphalt road running vertically through the right side of the image, with yellow center lines and white lane markings. Several vehicles can be seen traveling or parked along it."
    },
    {
      "landmark_name": "building",
      "position": "top-left",
      "visual_description": "A structure with distinctive orange/terracotta roof tiles surrounded by trees and vegetation. The building appears to be a residential or small commercial property with a courtyard area."
    },
    {
      "landmark_name": "pedestrian walkway",
      "position": "middle",
      "visual_description": "A covered walkway or bridge structure with white railings and a brown/reddish walking surface, connecting different areas of what appears to be a recreational complex."
    },
    {
      "landmark_name": "paved plaza",
      "position": "left",
      "visual_description": "A large paved area with a reddish-pink grid pattern, likely a public square or gathering space adjacent to the sports facilities."
    }
  ],
  "anomalies": [
    {
      "anomaly_name": "damaged court surface",
      "position": "middle",
      "visual_description": "The sports court shows signs of wear and deterioration, with faded paint, discolored patches, and what appears to be water damage or weathering on the playing surface, particularly visible on the right side of the court."
    },
    {
      "anomaly_name": "overgrown vegetation",
      "position": "top-left",
      "visual_description": "Areas of dense, unmanaged vegetation and trees encroaching on the developed spaces, suggesting lack of maintenance in certain sections of the property."
    }
  ],
  "visibility": {
    "weather": "sunny",
    "background_scene": "city"
  }
}
```

```json
{
  "landmarks": [
    {
      "landmark_name": "basketball court",
      "position": "middle",
      "visual_description": "A green and blue multi-purpose sports court with white line markings for basketball. The court has a distinctive blue perimeter and green playing surface with visible basketball hoops."
    },
    {
      "landmark_name": "road",
      "position": "right",
      "visual_description": "A wide multi-lane asphalt road running vertically through the right side of the image, with yellow center lines and white lane markings. Several vehicles can be seen traveling or parked along it."
    },
    {
      "landmark_name": "building",
      "position": "top-left",
      "visual_description": "A structure with distinctive orange/terracotta roof tiles surrounded by trees and vegetation. The building appears to be a residential or small commercial property with a courtyard area."
    },
    {
      "landmark_name": "pedestrian walkway",
      "position": "middle",
      "visual_description": "A covered walkway or bridge structure with white railings and a brown/reddish walking surface, connecting different areas of what appears to be a recreational complex."
    },
    {
      "landmark_name": "paved plaza",
      "position": "left",
      "visual_description": "A large paved area with a reddish-pink grid pattern, likely a public square or gathering space adjacent to the sports facilities."
    }
  ],
  "anomalies": [
    {
      "anomaly_name": "damaged court surface",
      "position": "middle",
      "visual_description": "The sports court shows signs of wear and deterioration, with faded paint, discolored patches, and what appears to be water damage or weathering on the playing surface, particularly visible on the right side of the court."
    },
    {
      "anomaly_name": "overgrown vegetation",
      "position": "top-left",
      "visual_description": "Areas of dense, unmanaged vegetation and trees encroaching on the developed spaces, suggesting lack of maintenance in certain sections of the property."
    }
  ],
  "visibility": {
    "weather": "sunny",
    "background_scene": "city"
  }
}
```

```json
{
  "landmarks": [
    {
      "landmark_name": "temple",
      "position": "middle",
      "visual_description": "An ornate temple structure with distinctive orange/terracotta tiled roofs featuring multiple decorative peaks and pavilions. The building has a traditional East Asian architectural style with elaborate roof corners that curve upward."
    },
    {
      "landmark_name": "parking lot",
      "position": "top-left",
      "visual_description": "A large organized parking area with numerous white and colored vehicles arranged in neat rows on a reddish-brown paved surface."
    },
    {
      "landmark_name": "multi-lane road",
      "position": "right",
      "visual_description": "A wide, gray asphalt road with multiple lanes running vertically through the image, featuring clear lane markings and minimal traffic."
    },
    {
      "landmark_name": "forest patch",
      "position": "left",
      "visual_description": "Dense green foliage of trees and vegetation forming a substantial natural area along the left side of the image, providing contrast to the built environment."
    },
    {
      "landmark_name": "covered walkway",
      "position": "bottom",
      "visual_description": "A long, narrow structure with a light-colored roof that appears to be a covered walkway or corridor extending horizontally across the bottom portion of the image."
    }
  ],
  "anomalies": [
    {
      "anomaly_name": "construction area",
      "position": "bottom-left",
      "visual_description": "An unfinished or partially developed area with exposed ground, some construction materials, and irregular surface patterns indicating ongoing development work."
    }
  ],
  "visibility": {
    "weather": "sunny",
    "background_scene": "city"
  }
}
```

```json
{
  "landmarks": [
    {
      "landmark_name": "parking lot",
      "position": "left",
      "visual_description": "A large organized parking area with reddish-pink pavement containing multiple rows of predominantly white and dark-colored vehicles arranged in a structured pattern."
    },
    {
      "landmark_name": "road",
      "position": "right",
      "visual_description": "A wide multi-lane asphalt road with yellow lane markings, white pedestrian crossings, and clear traffic patterns running through the right portion of the image."
    },
    {
      "landmark_name": "building",
      "position": "bottom",
      "visual_description": "A structure with a distinctive bright red roof and orange/tan walls, possibly a commercial establishment or service building at the edge of the parking area."
    },
    {
      "landmark_name": "tree cluster",
      "position": "top-left",
      "visual_description": "A dense collection of green trees with full foliage creating a natural boundary along the left edge of the parking area, providing shade and natural contrast to the urban elements."
    }
  ],
  "anomalies": [
    {
      "anomaly_name": "construction area",
      "position": "bottom-left",
      "visual_description": "A disturbed ground area with exposed dirt, some construction materials, and partial development visible at the edge of the tree line and parking lot."
    }
  ],
  "visibility": {
    "weather": "sunny",
    "background_scene": "city"
  }
}
```
</details>

<details>
<summary>Gemini</summary>

# Gemini

```json
{
  "landmarks": [
    {
      "landmark_name": "buildings",
      "position": "top",
      "visual_description": "A cluster of buildings with orange tiled roofs, surrounded by trees and some smaller structures. The buildings appear to be of traditional design."
    },
    {
      "landmark_name": "road",
      "position": "right",
      "visual_description": "A wide, straight road with multiple lanes and yellow center lines. There are trees lining the side of the road and some parked cars are visible."
    },
    {
      "landmark_name": "basketball court",
      "position": "bottom-left",
      "visual_description": "A basketball court with blue and green painted surfaces. The court has clearly marked lines and hoops at each end."
    },
    {
      "landmark_name": "building",
      "position": "right",
      "visual_description": "A long, rectangular building with a light-colored roof and a row of windows. The building appears to be multi-storied and is located adjacent to the road."
    },
    {
      "landmark_name": "open court",
      "position": "middle",
      "visual_description": "An open court with a green surface, located next to the basketball court. The surface is worn and has some patches of discoloration."
    }
  ],
  "anomalies": [],
  "visibility": {
    "weather": "sunny",
    "background_scene": "city"
  }
}
```

```json
{
  "landmarks": [
    {
      "landmark_name": "parking lot",
      "position": "top-left",
      "visual_description": "A large parking lot filled with numerous cars, arranged in neat rows. The surface is paved with a reddish material, and the cars are of various colors including white, silver, and blue."
    },
    {
      "landmark_name": "temple complex",
      "position": "middle",
      "visual_description": "A traditional temple complex with multiple buildings. Some buildings have orange tiled roofs with ornate decorations, while others have red tiled roofs. The complex is surrounded by trees and gardens."
    },
    {
      "landmark_name": "road",
      "position": "right",
      "visual_description": "A wide, multi-lane road with white lane markings. Trees line the side of the road, casting shadows on the pavement. Cars are visible driving on the road."
    },
    {
      "landmark_name": "parking area",
      "position": "top-right",
      "visual_description": "A large paved parking area with painted parking space lines. Several vehicles are parked in the area, and there are some trees along the edge."
    },
    {
      "landmark_name": "building",
      "position": "bottom-right",
      "visual_description": "A multi-story building with a light-colored roof and multiple windows. The building appears to be modern in design."
    },
    {
      "landmark_name": "pool",
      "position": "bottom-left",
      "visual_description": "A rectangular pool with a light blue surface. The pool is surrounded by a paved area and a running track."
    }
  ],
  "anomalies": [],
  "visibility": {
    "weather": "sunny",
    "background_scene": "city"
  }
}
```

```json
{
  "landmarks": [
    {
      "landmark_name": "road",
      "position": "middle",
      "visual_description": "A wide, straight road with multiple lanes, marked with white lines and yellow center lines. A crosswalk is visible near the top of the image."
    },
    {
      "landmark_name": "parking lot",
      "position": "left",
      "visual_description": "A large parking lot filled with numerous cars, arranged in neat rows. The parking surface appears to be a reddish-brown color."
    },
    {
      "landmark_name": "parking lot",
      "position": "right",
      "visual_description": "A large parking lot filled with numerous cars, arranged in neat rows. The parking surface appears to be gray."
    },
    {
      "landmark_name": "building",
      "position": "bottom",
      "visual_description": "A building with a red tiled roof and a complex architectural design, possibly a temple or traditional structure."
    },
    {
      "landmark_name": "trees",
      "position": "left",
      "visual_description": "Dense green foliage of trees bordering the parking lot and road."
    },
    {
      "landmark_name": "trees",
      "position": "right",
      "visual_description": "Trees bordering the parking lot and road, casting shadows on the road surface."
    }
  ],
  "anomalies": [],
  "visibility": {
    "weather": "sunny",
    "background_scene": "city"
  }
}
```
</details>

</details>