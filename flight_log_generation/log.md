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

<details>
<summary>2025-04-30, test 3 cloud models to see how they handle JSON outputs (timeline involved, batch size 3)</summary>

<details>
<summary>ChatGPT</summary>

# ChatGPT

```json
{
  "frames": [
    {
      "frame_id": 1,
      "landmarks": [
        {
          "landmark_name": "basketball court",
          "position": "bottom-left",
          "visual_description": "A large outdoor basketball court with blue and green surfaces, surrounded by a fence."
        },
        {
          "landmark_name": "road",
          "position": "right",
          "visual_description": "A wide road with multiple lanes and a few parked cars along the side."
        },
        {
          "landmark_name": "building",
          "position": "top-right",
          "visual_description": "A building with a white roof and a checkered pattern on the side."
        }
      ],
      "anomalies": [],
      "visibility": {
        "weather": "sunny",
        "background_scene": "city"
      }
    },
    {
      "frame_id": 2,
      "landmarks": [
        {
          "landmark_name": "temple",
          "position": "top-left",
          "visual_description": "A traditional temple with orange-tiled roofs and intricate architectural details."
        },
        {
          "landmark_name": "parking lot",
          "position": "middle",
          "visual_description": "A parking lot filled with cars, organized in rows."
        },
        {
          "landmark_name": "road",
          "position": "right",
          "visual_description": "A wide road with multiple lanes, similar to the previous frame."
        }
      ],
      "anomalies": [],
      "visibility": {
        "weather": "sunny",
        "background_scene": "city"
      }
    },
    {
      "frame_id": 3,
      "landmarks": [
        {
          "landmark_name": "parking lot",
          "position": "top-left",
          "visual_description": "A large parking lot with numerous cars parked in rows."
        },
        {
          "landmark_name": "road",
          "position": "right",
          "visual_description": "A wide road with multiple lanes, consistent with previous frames."
        }
      ],
      "anomalies": [],
      "visibility": {
        "weather": "sunny",
        "background_scene": "city"
      }
    }
  ],
  "motion": [
    {
      "from_frame": 1,
      "to_frame": 2,
      "movement_direction": "top-right"
    },
    {
      "from_frame": 2,
      "to_frame": 3,
      "movement_direction": "top-right"
    }
  ],
  "inference": [
    {
      "type": "landmark",
      "name": "road",
      "frame_pair": [1, 2],
      "inference_probability": 0.95
    },
    {
      "type": "landmark",
      "name": "road",
      "frame_pair": [2, 3],
      "inference_probability": 0.95
    },
    {
      "type": "landmark",
      "name": "parking lot",
      "frame_pair": [2, 3],
      "inference_probability": 0.90
    }
  ]
}
```
</details>

<details>
<summary>Claude</summary>

# Claude

```json
{
  "frames": [
    {
      "frame_id": 1,
      "landmarks": [
        {
          "landmark_name": "basketball court",
          "position": "middle",
          "visual_description": "A green basketball court with blue borders, white court markings, and visible hoops at both ends."
        },
        {
          "landmark_name": "covered walkway",
          "position": "middle",
          "visual_description": "A long wooden walkway with white railings and roof structure connecting different areas of the complex."
        },
        {
          "landmark_name": "multi-lane road",
          "position": "right",
          "visual_description": "A wide asphalt road with multiple lanes and yellow center line markings."
        },
        {
          "landmark_name": "temple building",
          "position": "top-left",
          "visual_description": "A traditional Asian-style building with distinctive orange/terracotta tiled roofs and ornate architectural details."
        },
        {
          "landmark_name": "commercial building",
          "position": "right",
          "visual_description": "A long rectangular building with a light blue/white roof and multiple units or sections."
        },
        {
          "landmark_name": "paved plaza",
          "position": "bottom-left",
          "visual_description": "A large paved area with reddish-brown tiles arranged in a grid pattern."
        },
        {
          "landmark_name": "green space",
          "position": "left",
          "visual_description": "Dense area of trees and vegetation forming a green buffer zone."
        }
      ],
      "anomalies": [],
      "visibility": {
        "weather": "sunny",
        "background_scene": "city"
      }
    },
    {
      "frame_id": 2,
      "landmarks": [
        {
          "landmark_name": "temple building",
          "position": "middle-left",
          "visual_description": "A traditional Asian-style temple complex with multiple orange/terracotta tiled roofs, ornate details, and decorative elements."
        },
        {
          "landmark_name": "parking lot",
          "position": "top-left",
          "visual_description": "An organized parking area with numerous white and some colored vehicles arranged in rows on reddish pavement."
        },
        {
          "landmark_name": "multi-lane road",
          "position": "right",
          "visual_description": "A wide asphalt road with multiple lanes and yellow center line markings."
        },
        {
          "landmark_name": "covered walkway",
          "position": "bottom",
          "visual_description": "A wooden walkway with white railings and roof structure partially visible at the bottom of the frame."
        },
        {
          "landmark_name": "green space",
          "position": "left",
          "visual_description": "Dense area of trees and vegetation forming a green buffer zone."
        },
        {
          "landmark_name": "commercial building",
          "position": "bottom-right",
          "visual_description": "Part of a rectangular building with a light blue/white roof visible at the edge of the frame."
        },
        {
          "landmark_name": "red-roofed building",
          "position": "middle",
          "visual_description": "A structure with a distinctive bright red metal roof adjacent to the temple complex."
        }
      ],
      "anomalies": [],
      "visibility": {
        "weather": "sunny",
        "background_scene": "city"
      }
    },
    {
      "frame_id": 3,
      "landmarks": [
        {
          "landmark_name": "parking lot",
          "position": "middle-left",
          "visual_description": "A large parking area with numerous white and some colored vehicles arranged in neat rows on reddish pavement."
        },
        {
          "landmark_name": "multi-lane road",
          "position": "middle-right",
          "visual_description": "A wide asphalt road with multiple lanes, yellow center line markings, and visible crosswalk stripes at an intersection."
        },
        {
          "landmark_name": "temple building",
          "position": "bottom-left",
          "visual_description": "Partial view of a traditional Asian-style building with orange/terracotta tiled roof, only a corner is visible."
        },
        {
          "landmark_name": "red-roofed building",
          "position": "bottom",
          "visual_description": "Partial view of a structure with a distinctive bright red metal roof."
        },
        {
          "landmark_name": "green space",
          "position": "left",
          "visual_description": "Area with trees and vegetation along the left edge of the frame."
        },
        {
          "landmark_name": "parking lot 2",
          "position": "right",
          "visual_description": "Another parking area on the right side with vehicles arranged in a more scattered pattern."
        }
      ],
      "anomalies": [],
      "visibility": {
        "weather": "sunny",
        "background_scene": "city"
      }
    }
  ],
  "motion": [
    {
      "from_frame": 1,
      "to_frame": 2,
      "movement_direction": "top-left"
    },
    {
      "from_frame": 2,
      "to_frame": 3,
      "movement_direction": "top"
    }
  ],
  "inference": [
    {
      "type": "landmark",
      "name": "temple building",
      "frame_pair": [1, 2],
      "inference_probability": 0.95
    },
    {
      "type": "landmark",
      "name": "multi-lane road",
      "frame_pair": [1, 2],
      "inference_probability": 0.98
    },
    {
      "type": "landmark",
      "name": "covered walkway",
      "frame_pair": [1, 2],
      "inference_probability": 0.90
    },
    {
      "type": "landmark",
      "name": "green space",
      "frame_pair": [1, 2],
      "inference_probability": 0.95
    },
    {
      "type": "landmark",
      "name": "commercial building",
      "frame_pair": [1, 2],
      "inference_probability": 0.85
    },
    {
      "type": "landmark",
      "name": "temple building",
      "frame_pair": [2, 3],
      "inference_probability": 0.85
    },
    {
      "type": "landmark",
      "name": "parking lot",
      "frame_pair": [2, 3],
      "inference_probability": 0.98
    },
    {
      "type": "landmark",
      "name": "multi-lane road",
      "frame_pair": [2, 3],
      "inference_probability": 0.98
    },
    {
      "type": "landmark",
      "name": "red-roofed building",
      "frame_pair": [2, 3],
      "inference_probability": 0.90
    },
    {
      "type": "landmark",
      "name": "green space",
      "frame_pair": [2, 3],
      "inference_probability": 0.90
    }
  ]
}
```
</details>

<details>
<summary>Gemini</summary>

# Gemini

```json
{
  "frames": [
    {
      "frame_id": 1,
      "landmarks": [
        {
          "landmark_name": "basketball court",
          "position": "bottom-left",
          "visual_description": "A rectangular basketball court with blue and green painted surfaces, white lines marking the boundaries and key areas, and basketball hoops at each end."
        },
        {
          "landmark_name": "multi-purpose court",
          "position": "middle",
          "visual_description": "A rectangular multi-purpose court with a green painted surface and curved blue lines along one side. It appears to be adjacent to the basketball court."
        },
        {
          "landmark_name": "road",
          "position": "right",
          "visual_description": "A wide, straight road with multiple lanes, marked by white lines. There are trees lining the side of the road."
        },
        {
          "landmark_name": "buildings",
          "position": "top-right",
          "visual_description": "A row of low-rise buildings with white walls and gray roofs, located along the right side of the road."
        },
        {
          "landmark_name": "traditional buildings",
          "position": "top-left",
          "visual_description": "A cluster of traditional buildings with orange tiled roofs, located near trees and a paved area."
        },
        {
          "landmark_name": "trees",
          "position": "left",
          "visual_description": "A dense patch of green trees located near the basketball court and traditional buildings."
        }
      ],
      "anomalies": [],
      "visibility": {
        "weather": "sunny",
        "background_scene": "city"
      }
    },
    {
      "frame_id": 2,
      "landmarks": [
        {
          "landmark_name": "parking lot",
          "position": "top-left",
          "visual_description": "A large parking lot filled with many cars, mostly white and silver. It is located next to the traditional buildings."
        },
        {
          "landmark_name": "traditional buildings",
          "position": "top",
          "visual_description": "A cluster of traditional buildings with orange and red tiled roofs. They are located next to the parking lot and a road."
        },
        {
          "landmark_name": "road",
          "position": "right",
          "visual_description": "A wide, straight road with multiple lanes, marked by white lines. There are trees lining the side of the road."
        },
        {
          "landmark_name": "buildings",
          "position": "right",
          "visual_description": "A row of low-rise buildings with white walls and gray roofs, located along the right side of the road."
        },
        {
          "landmark_name": "basketball court",
          "position": "bottom-left",
          "visual_description": "A rectangular basketball court with blue and green painted surfaces, white lines marking the boundaries and key areas, and basketball hoops at each end."
        },
        {
          "landmark_name": "multi-purpose court",
          "position": "bottom",
          "visual_description": "A rectangular multi-purpose court with a green painted surface and curved blue lines along one side. It appears to be adjacent to the basketball court."
        },
        {
          "landmark_name": "trees",
          "position": "left",
          "visual_description": "A dense patch of green trees located near the parking lot and traditional buildings."
        }
      ],
      "anomalies": [],
      "visibility": {
        "weather": "sunny",
        "background_scene": "city"
      }
    },
    {
      "frame_id": 3,
      "landmarks": [
        {
          "landmark_name": "parking lot",
          "position": "left",
          "visual_description": "A large parking lot filled with many cars, mostly white and silver. It is located next to the traditional buildings."
        },
        {
          "landmark_name": "traditional buildings",
          "position": "bottom-left",
          "visual_description": "A cluster of traditional buildings with orange and red tiled roofs. They are located next to the parking lot and a road."
        },
        {
          "landmark_name": "road",
          "position": "middle",
          "visual_description": "A wide, straight road with multiple lanes, marked by white lines. There are trees lining the side of the road."
        },
        {
          "landmark_name": "buildings",
          "position": "right",
          "visual_description": "A row of low-rise buildings with white walls and gray roofs, located along the right side of the road."
        },
        {
          "landmark_name": "parking lot",
          "position": "right",
          "visual_description": "A parking lot filled with many cars, mostly white and silver. It is located next to the buildings."
        },
        {
          "landmark_name": "trees",
          "position": "left",
          "visual_description": "A dense patch of green trees located near the parking lot and traditional buildings."
        }
      ],
      "anomalies": [],
      "visibility": {
        "weather": "sunny",
        "background_scene": "city"
      }
    }
  ],
  "motion": [
    {
      "from_frame": 1,
      "to_frame": 2,
      "movement_direction": "top-left"
    },
    {
      "from_frame": 2,
      "to_frame": 3,
      "movement_direction": "bottom-left"
    }
  ],
  "inference": [
    {
      "type": "landmark",
      "name": "basketball court",
      "frame_pair": [
        1,
        2
      ],
      "inference_probability": 0.95
    },
    {
      "type": "landmark",
      "name": "multi-purpose court",
      "frame_pair": [
        1,
        2
      ],
      "inference_probability": 0.95
    },
    {
      "type": "landmark",
      "name": "road",
      "frame_pair": [
        1,
        2
      ],
      "inference_probability": 0.99
    },
    {
      "type": "landmark",
      "name": "buildings",
      "frame_pair": [
        1,
        2
      ],
      "inference_probability": 0.99
    },
    {
      "type": "landmark",
      "name": "traditional buildings",
      "frame_pair": [
        1,
        2
      ],
      "inference_probability": 0.98
    },
    {
      "type": "landmark",
      "name": "trees",
      "frame_pair": [
        1,
        2
      ],
      "inference_probability": 0.98
    },
    {
      "type": "landmark",
      "name": "traditional buildings",
      "frame_pair": [
        2,
        3
      ],
      "inference_probability": 0.98
    },
    {
      "type": "landmark",
      "name": "road",
      "frame_pair": [
        2,
        3
      ],
      "inference_probability": 0.99
    },
    {
      "type": "landmark",
      "name": "buildings",
      "frame_pair": [
        2,
        3
      ],
      "inference_probability": 0.99
    },
    {
      "type": "landmark",
      "name": "trees",
      "frame_pair": [
        2,
        3
      ],
      "inference_probability": 0.98
    },
    {
      "type": "landmark",
      "name": "parking lot",
      "frame_pair": [
        2,
        3
      ],
      "inference_probability": 0.98
    }
  ]
}
```
</details>

</details>