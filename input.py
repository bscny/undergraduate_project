from datetime import datetime
import cv2

from output import drone_print

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
    
def input_direction():
    """
    Interactive direction selector with 8 directions.
    Returns an ID (0-7) representing the chosen direction.
    
    Direction mapping:
    0: Top
    1: Top-Right
    2: Right
    3: Bottom-Right
    4: Bottom
    5: Bottom-Left
    6: Left
    7: Top-Left
    """
    directions = [
        "Top",
        "Top-Right",
        "Right",
        "Bottom-Right",
        "Bottom",
        "Bottom-Left",
        "Left",
        "Top-Left"
    ]

    drone_print("SELECT DIRECTION")
    drone_print("="*40, show_role=False)
    
    # Display options in a grid layout
    drone_print("\n   7. Top-Left      0. Top      1. Top-Right", show_role=False)
    drone_print("            \\        |        /", show_role=False)
    drone_print("             \\       |       /", show_role=False)
    drone_print("   6. Left  --------( )--------  2. Right", show_role=False)
    drone_print("             /       |       \\", show_role=False)
    drone_print("            /        |        \\", show_role=False)
    drone_print("5. Bottom-Left   4. Bottom   3. Bottom-Right\n", show_role=False)
    
    drone_print("-"*40, show_role=False)
    for i, direction in enumerate(directions):
        drone_print(f"{i}. {direction}", show_role=False)
    drone_print("-"*40, show_role=False)
    
    while True:
        try:
            drone_print("Enter your choice (0-7):")
            choice = input().strip()
            
            if not choice.isdigit():
                drone_print("❌ Please enter a number between 0 and 7")
                continue
            
            choice_id = int(choice)
            
            if 0 <= choice_id <= 7:
                drone_print(f"✓ Selected: {directions[choice_id]} (ID: {choice_id})")
                return choice_id
            else:
                drone_print("❌ Please enter a number between 0 and 7")
                
        # except KeyboardInterrupt:
        #     drone_print("\n\n⚠ Selection cancelled")
        #     return None
        except Exception as e:
            drone_print(f"❌ Error: {e}")
            continue
        
def input_scanning_area():
    """
    Interactive area selector with 9 options.
    Returns an ID (0-8) representing the chosen direction.
    
    Direction mapping:
    0: scan around
    1: scan ahead
    2: scan behind
    3: scan left
    4: scan right
    5: scan front-left
    6: scan front-right
    7: scan back-left
    8: scan back-right
    """
    options = [
        "Scan Around",
        "Scan Ahead",
        "Scan Behind",
        "Scan Left",
        "Scan Right",
        "Scan Front-Left",
        "Scan Front-Right",
        "Scan Back-Left",
        "Scan Back-Right"
    ]

    drone_print("SELECT SCANNING TYPE")
    drone_print("="*40, show_role=False)
    drone_print("() Represents the drone!\n", show_role=False)
    
    drone_print("..........", show_role=False)
    drone_print(": 0      :", show_role=False)
    drone_print(":   ()   :", show_role=False)
    drone_print(":        :", show_role=False)
    drone_print("..........\n", show_role=False)

    drone_print("       ..........", show_role=False)
    drone_print("       :   1    :", show_role=False)
    drone_print(".......:..    ..:.......", show_role=False)
    drone_print(":      : :    : :      :", show_role=False)
    drone_print(":   3  ..:.().:..   4  :", show_role=False)
    drone_print(":      : :    : :      :", show_role=False)
    drone_print(".......:..    ..:.......", show_role=False)
    drone_print("       :    2   :", show_role=False)
    drone_print("       ..........\n", show_role=False)
    
    drone_print("...................", show_role=False)
    drone_print(":        :        :", show_role=False)
    drone_print(":   5    :   6    :", show_role=False)
    drone_print(":        :        :", show_role=False)
    drone_print(":.......()........:", show_role=False)
    drone_print(":        :        :", show_role=False)
    drone_print(":   7    :   8    :", show_role=False)
    drone_print(":        :        :", show_role=False)
    drone_print("...................\n", show_role=False)
    
    drone_print("-"*40, show_role=False)
    for i, option in enumerate(options):
        drone_print(f"{i}. {option}", show_role=False)
    drone_print("-"*40, show_role=False)
    
    while True:
        try:
            drone_print("Enter your choice (0-8):")
            choice = input().strip()
            
            if not choice.isdigit():
                drone_print("❌ Please enter a number between 0 and 8")
                continue
            
            choice_id = int(choice)
            
            if 0 <= choice_id <= 8:
                drone_print(f"Selected: {options[choice_id]}")
                return choice_id
            else:
                drone_print("❌ Please enter a number between 0 and 8")
        except Exception as e:
            drone_print(f"❌ Error: {e}")
        
# Example usage
if __name__ == "__main__":
    # Input flight log data
    formatted_string = input_drone_flight_log("assets/large_files/videos/simcity.mp4")
    
    # Display the formatted string
    print("\n" + "=" * 50)
    print("GENERATED FLIGHT LOG")
    print("=" * 50)
    print(formatted_string)
    
    print("Flight log entry complete!")