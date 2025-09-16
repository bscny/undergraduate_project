from datetime import datetime
import cv2

def input_drone_flight_log(video_path):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Error: Could not open video during input.")
        exit()
        
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    w  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    print("=== DRONE FLIGHT LOG DATA ENTRY ===\n")
    
    # Flight Identification
    print("FLIGHT IDENTIFICATION")
    print("-" * 20)
    
    # Get date with validation
    while True:
        date_input = input("Date (YYYY-MM-DD or press Enter for today): ").strip()
        if not date_input:
            date_input = datetime.now().strftime("%Y-%m-%d")
            break
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
    
    start_time = input("Start Time (HH:MM): ").strip()
    end_time = input("End Time (HH:MM): ").strip()
    duration_sec = frame_count / fps if fps > 0 else 0
    minutes = int(duration_sec // 60)
    seconds = int(duration_sec % 60)
    total_duration = f"{minutes} min {seconds} sec"
    
    print("\nFLIGHT PURPOSE & OPERATIONS")
    print("-" * 27)
    
    purpose = input("Purpose of Flight: ").strip()
    operation_type = input("Type of Operation: ").strip()
    
    print("\nLOCATION & ENVIRONMENT")
    print("-" * 22)
    
    location_name = input("Location Name/Description: ").strip()
    gps_takeoff = input("GPS Coordinates (Takeoff): ").strip()
    gps_landing = input("GPS Coordinates (Landing): ").strip()
    
    print("\nCAMERA & RECORDING SETTINGS")
    print("-" * 27)
    
    video_resolution = f"{w}x{h}"
    frame_rate = fps
    recording_format = input("Recording Format (e.g., MP4, MOV): ").strip()
    
    # Create formatted string content
    formatted_content = f"""# DRONE FLIGHT LOG

## FLIGHT IDENTIFICATION

**Date:** {date_input}
**Start Time:** {start_time}
**End Time:** {end_time}
**Total Duration:** {total_duration}

## FLIGHT PURPOSE & OPERATIONS

**Purpose of Flight:** {purpose}
**Type of Operation:** {operation_type}

## LOCATION & ENVIRONMENT

**Location Name/Description:** {location_name}
**GPS Coordinates (Takeoff):** {gps_takeoff}
**GPS Coordinates (Landing):** {gps_landing}

## CAMERA & RECORDING SETTINGS

**Video Resolution:** {video_resolution}
**Frame Rate:** {frame_rate} fps
**Recording Format:** {recording_format}
"""
    
    return formatted_content



# Example usage
if __name__ == "__main__":
    # Input flight log data
    formatted_string = input_drone_flight_log("assets/large_files/videos/city.MP4")
    
    # Display the formatted string
    print("\n" + "=" * 50)
    print("GENERATED FLIGHT LOG")
    print("=" * 50)
    print(formatted_string)
    
    print("Flight log entry complete!")