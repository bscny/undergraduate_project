from colorama import Fore, Back, Style, init

def init_colorama():
    """Initializes colorama for cross-platform support."""
    init(autoreset=True)

def system_print(message, show_role=True, end="\n"):
    """
    Prints a message with a 'system' style.
    Uses yellow text to indicate warnings, notifications, or system status.
    
    Args:
        message (str): The message to be printed.
        show_role (bool): If True, prepends the [ROLE] to the message.
        end (str): The character to print at the end of the line.
    """
    prefix = f"{Style.NORMAL}{Fore.YELLOW}[SYSTEM] " if show_role else ""
    print(f"{prefix}{Fore.YELLOW}{message}", end=end)

def drone_print(message, show_role=True, end="\n"):
    """
    Prints a message with a 'drone' or 'bot' style.
    Uses cyan text for a futuristic, automated feel, representing data or logs.
    
    Args:
        message (str): The message to be printed.
        show_role (bool): If True, prepends the [ROLE] to the message.
        end (str): The character to print at the end of the line.
    """
    prefix = f"{Style.NORMAL}{Fore.CYAN}[DRONE] " if show_role else ""
    print(f"{prefix}{Fore.CYAN}{message}", end=end)

def user_print(message, show_role=True, end="\n"):
    """
    Prints a message with a 'user' style.
    Uses bright white text to represent user input or direct communication.
    
    Args:
        message (str): The message to be printed.
        show_role (bool): If True, prepends the [ROLE] to the message.
        end (str): The character to print at the end of the line.
    """
    prefix = f"{Style.BRIGHT}{Fore.WHITE}[USER] " if show_role else ""
    print(f"{prefix}{Style.NORMAL}{Fore.WHITE}{message}", end=end)

if __name__ == '__main__':
    # Initialize colorama once at the start of the script
    init_colorama()
    
    print("--- Simulating a Drone Operation Log ---\n")
    
    system_print("Initializing drone connection...")
    drone_print("Battery at 98%. GPS lock acquired.")
    drone_print("Propellers engaged. Ready for takeoff.")
    system_print("Drone is airborne. Mission started.")
    user_print("Command received: Proceed to waypoint alpha.")
    drone_print("Executing flight path to waypoint alpha...")
    system_print("WARNING: High wind speeds detected.")
    drone_print("Adjusting flight stability controls.")
    user_print("Hold position and report status.")
    drone_print("Maintaining current position. All systems nominal.")
    system_print("Mission complete. Returning to launch point.")
    
    print("\n\n--- Demonstrating New Parameters ---")
    system_print("Status check: ", end="")
    # The next message will appear on the same line and without a prefix
    system_print("OK.", show_role=False) 
    
    user_print("This message will not have the [USER] prefix.", show_role=False)
    
    print("\n--- Simulation Complete ---")

