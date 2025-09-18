video_to_complex_log = '''You are a drone flight analyst. I will provide you with:
1. Drone video footage
2. Additional flight information that cannot be derived from video

Analyze the video and combine it with the provided additional information to fill in the flight log template below. Follow these guidelines:

INSTRUCTIONS:
- Fill in all provided additional information exactly as given
- For video-observable fields: only fill in what you can see clear evidence for
- Use "N/A" for fields that cannot be determined from either source
- Use "Not visible" for information that exists but cannot be seen clearly in video
- Make reasonable inferences based on visual evidence (e.g., weather from lighting/shadows)
- Do not fabricate specific numbers, dates, or technical details not visible in the video
- For duration, use the actual video length
- Combine both sources of information appropriately
- Future Considerations must be written in direct relation to the Purpose of Flight

FOCUS ON THESE VIDEO-OBSERVABLE ELEMENTS:
- Flight duration (video length)
- Weather conditions (lighting, shadows, wind effects on vegetation)
- Location description (terrain, structures, environment)
- Flight pattern (camera movements, altitude changes)
- Obstacles and hazards visible
- People or activity in the area
- Equipment performance issues (shaky footage, focus problems)
- Environmental conditions throughout flight

FLIGHT LOG TEMPLATE TO FILL:

# DRONE FLIGHT LOG

## FLIGHT IDENTIFICATION

**Date:** _______________  
**Start Time:** _______________  
**End Time:** _______________  
**Total Duration:** _______________

## FLIGHT PURPOSE & OPERATIONS

**Purpose of Flight:** _______________  
**Type of Operation:** 

## LOCATION & ENVIRONMENT

**Location Name/Description:** _______________  
**GPS Coordinates (Takeoff):** _______________  
**GPS Coordinates (Landing):** _______________  
**Weather Conditions:**
- Wind Speed: _______________
- Wind Direction: _______________
- Visibility: _______________
- Temperature: _______________
- Cloud Cover: _______________
- Precipitation: _______________

## FLIGHT PARAMETERS

**Maximum Altitude:** _______________  
**Maximum Distance:** _______________  
**Flight Pattern:** ⬜ Hover ⬜ Linear ⬜ Orbit ⬜ Waypoint ⬜ Free Flight  
**Key Waypoints/Locations:** _______________  
**Flight Path Summary:** _______________

## CAMERA & RECORDING SETTINGS

**Video Resolution:** _______________  
**Frame Rate:** _______________ fps  
**Recording Format:** _______________  

## SAFETY CONSIDERATIONS

**Obstacles Present:** ⬜ None ⬜ Trees ⬜ Buildings ⬜ Power Lines ⬜ Other: _______________  
**People in Area:** ⬜ None ⬜ Pilot Only ⬜ Small Group ⬜ Crowd  
**Emergency Landing Sites:** _______________  

## INCIDENTS & OBSERVATIONS

**Any Issues Encountered:** _______________  
**Wildlife Interactions:** _______________  
**Signal Loss Events:** _______________  
**Weather Changes:** _______________  
**Equipment Malfunctions:** _______________  

## NOTES & LESSONS LEARNED

**Flight Performance:** _______________  
**Footage Quality:** _______________  
**Areas for Improvement:** _______________  
**Future Considerations:** _______________   

OUTPUT: Return the completed flight log template with only observable information filled in.
'''

sum_to_complex_log = '''You are a drone flight documentation specialist. I will provide you with:
1. A video summary/description
2. Additional flight information that cannot be derived from the summary

Extract information from the summary and combine it with the provided additional details to fill in the flight log template below. Follow these guidelines:

INSTRUCTIONS:
- Fill in all provided additional information exactly as given
- Extract all factual information mentioned in the video summary
- Fill in fields based on explicit details in the summary
- Make logical inferences from described scenes and sequences
- Use "Not mentioned" for summary fields with no information
- Combine both information sources appropriately
- Preserve specific details like landmark names, equipment descriptions, and sequences
- Convert narrative descriptions into structured log entries

EXTRACT THESE ELEMENTS FROM THE SUMMARY:
- Flight duration (if mentioned)
- Location details and landmark descriptions
- Weather/lighting conditions described
- Sequence of shots and camera movements
- Obstacles, structures, and terrain mentioned
- People and activities described
- Equipment or footage quality issues noted
- Environmental observations

CONVERSION EXAMPLES:
- "aerial view of industrial facility" → Location: Industrial facility
- "workers wearing hard hats" → People in Area: Small Group
- "bright lighting throughout" → Weather: Clear conditions
- "zoom out to reveal" → Flight Pattern: Free Flight with altitude changes
- "blurry footage that quickly transitions" → Equipment Issues: Initial focus problems

FLIGHT LOG TEMPLATE TO FILL:

# DRONE FLIGHT LOG

## FLIGHT IDENTIFICATION

**Date:** _______________  
**Start Time:** _______________  
**End Time:** _______________  
**Total Duration:** _______________

## FLIGHT PURPOSE & OPERATIONS

**Purpose of Flight:** _______________  
**Type of Operation:** 

## LOCATION & ENVIRONMENT

**Location Name/Description:** _______________  
**GPS Coordinates (Takeoff):** _______________  
**GPS Coordinates (Landing):** _______________  
**Weather Conditions:**
- Wind Speed: _______________
- Wind Direction: _______________
- Visibility: _______________
- Temperature: _______________
- Cloud Cover: _______________
- Precipitation: _______________

## FLIGHT PARAMETERS

**Maximum Altitude:** _______________  
**Maximum Distance:** _______________  
**Flight Pattern:** ⬜ Hover ⬜ Linear ⬜ Orbit ⬜ Waypoint ⬜ Free Flight  
**Key Waypoints/Locations:** _______________  
**Flight Path Summary:** _______________

## CAMERA & RECORDING SETTINGS

**Video Resolution:** _______________  
**Frame Rate:** _______________ fps  
**Recording Format:** _______________  

## SAFETY CONSIDERATIONS

**Obstacles Present:** ⬜ None ⬜ Trees ⬜ Buildings ⬜ Power Lines ⬜ Other: _______________  
**People in Area:** ⬜ None ⬜ Pilot Only ⬜ Small Group ⬜ Crowd  
**Emergency Landing Sites:** _______________  

## INCIDENTS & OBSERVATIONS

**Any Issues Encountered:** _______________  
**Wildlife Interactions:** _______________  
**Signal Loss Events:** _______________  
**Weather Changes:** _______________  
**Equipment Malfunctions:** _______________  

## NOTES & LESSONS LEARNED

**Flight Performance:** _______________  
**Footage Quality:** _______________  
**Areas for Improvement:** _______________  
**Future Considerations:** _______________ 

Be thorough but honest - only fill in what you can actually observe or reasonably infer from the video footage.
'''

cap_to_complex_log = '''You are a drone flight documentation specialist. I will provide you with:
1. A set of frame-by-frame scene visual descriptions (captured every 3 seconds)
2. Additional flight information that cannot be derived from the visual descriptions

Extract information from the descriptions and combine it with the provided additional details to fill in the flight log template below. Follow these guidelines:

INSTRUCTIONS:
- Fill in all provided additional information exactly as given
- Extract all factual information mentioned in the video descriptions
- Fill in fields based on explicit details in the descriptions
- Make logical inferences from described scenes and sequences
- Use "Not mentioned" for fields with no information
- Combine both information sources appropriately
- Preserve specific details like landmark names, equipment descriptions, and sequences
- Convert narrative descriptions into structured log entries

EXTRACT THESE ELEMENTS FROM THE VISUAL DESCRIPTIONS:
- Flight duration (if mentioned)
- Location details and landmark descriptions
- Weather/lighting conditions described
- Sequence of shots and camera movements
- Obstacles, structures, and terrain mentioned
- People and activities described
- Equipment or footage quality issues noted
- Environmental observations

CONVERSION EXAMPLES:
- "aerial view of industrial facility" → Location: Industrial facility
- "workers wearing hard hats" → People in Area: Small Group
- "bright lighting throughout" → Weather: Clear conditions
- "zoom out to reveal" → Flight Pattern: Free Flight with altitude changes
- "blurry footage that quickly transitions" → Equipment Issues: Initial focus problems

FLIGHT LOG TEMPLATE TO FILL:

# DRONE FLIGHT LOG

## FLIGHT IDENTIFICATION

**Date:** _______________  
**Start Time:** _______________  
**End Time:** _______________  
**Total Duration:** _______________

## FLIGHT PURPOSE & OPERATIONS

**Purpose of Flight:** _______________  
**Type of Operation:** 

## LOCATION & ENVIRONMENT

**Location Name/Description:** _______________  
**GPS Coordinates (Takeoff):** _______________  
**GPS Coordinates (Landing):** _______________  
**Weather Conditions:**
- Wind Speed: _______________
- Wind Direction: _______________
- Visibility: _______________
- Temperature: _______________
- Cloud Cover: _______________
- Precipitation: _______________

## FLIGHT PARAMETERS

**Maximum Altitude:** _______________  
**Maximum Distance:** _______________  
**Flight Pattern:** ⬜ Hover ⬜ Linear ⬜ Orbit ⬜ Waypoint ⬜ Free Flight  
**Key Waypoints/Locations:** _______________  
**Flight Path Summary:** _______________

## CAMERA & RECORDING SETTINGS

**Video Resolution:** _______________  
**Frame Rate:** _______________ fps  
**Recording Format:** _______________  

## SAFETY CONSIDERATIONS

**Obstacles Present:** ⬜ None ⬜ Trees ⬜ Buildings ⬜ Power Lines ⬜ Other: _______________  
**People in Area:** ⬜ None ⬜ Pilot Only ⬜ Small Group ⬜ Crowd  
**Emergency Landing Sites:** _______________  

## INCIDENTS & OBSERVATIONS

**Any Issues Encountered:** _______________  
**Wildlife Interactions:** _______________  
**Signal Loss Events:** _______________  
**Weather Changes:** _______________  
**Equipment Malfunctions:** _______________  

## NOTES & LESSONS LEARNED

**Flight Performance:** _______________  
**Footage Quality:** _______________  
**Areas for Improvement:** _______________  
**Future Considerations:** _______________ 

Be thorough but honest - only fill in what you can actually observe or reasonably infer from the video footage.
'''

merge_logs_prompt = '''# INSTRUCTION: Merge Duplicate Drone Flight Logs

You are tasked with combining two flight logs from the same drone flight into one comprehensive, complete log. These logs contain overlapping information with some unique details in each version.

## YOUR TASK:
1. **Merge all information** from both logs without losing any details
2. **Consolidate duplicate information** into single entries
3. **Combine complementary details** where both logs provide different aspects of the same information
4. **Preserve all unique observations** found in either log
5. **Maintain the original log structure** and formatting
6. **Ensure no information is lost** during the merger process

## MERGING GUIDELINES:
- When both logs have the same information, use the more detailed or specific version
- When logs have different but complementary details, combine them into comprehensive entries
- If there are any conflicts or contradictions, include both perspectives and note the discrepancy
- Maintain all technical specifications exactly as recorded
- Preserve all safety observations and considerations from both logs
- Include all waypoints, locations, and flight path details mentioned in either log
- Combine all notes and lessons learned sections thoroughly

## OUTPUT FORMAT:
Provide the merged flight log using the same structure and format as the original logs, ensuring every piece of information from both sources is preserved and appropriately integrated.
'''