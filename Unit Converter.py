"""
░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░████████╗███████╗██████╗░
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝░░░██║░░░█████╗░░██████╔╝
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░░░██║░░░██╔══╝░░██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""

class Colors:
    # Text colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Bright text colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'

    # Bright background colors
    BG_BRIGHT_BLACK = '\033[100m'
    BG_BRIGHT_RED = '\033[101m'
    BG_BRIGHT_GREEN = '\033[102m'
    BG_BRIGHT_YELLOW = '\033[103m'
    BG_BRIGHT_BLUE = '\033[104m'
    BG_BRIGHT_MAGENTA = '\033[105m'
    BG_BRIGHT_CYAN = '\033[106m'
    BG_BRIGHT_WHITE = '\033[107m'
    
    # Style formatting
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSED = '\033[7m'
    HIDDEN = '\033[8m'

    # Reset
    RESET = '\033[0m'

    # Combinations
    TITLE = BRIGHT_CYAN + BOLD
    PROMPT = BRIGHT_GREEN
    ERROR = BRIGHT_RED + BOLD
    SUCCESS = BRIGHT_GREEN + BOLD
    RESULT = YELLOW + BOLD
    SEPARATOR = BRIGHT_BLUE


def print_header():
    """Prints a nice header for the application"""
    print(Colors.TITLE + """
╔═══════════════════════════════════════════════╗
║               UNIT CONVERTER                  ║
║        Convert between various units          ║
╚═══════════════════════════════════════════════╝
""" + Colors.RESET)


def get_valid_input(prompt_text, valid_options=None, is_numeric=False):
    while True:
        print(Colors.PROMPT + prompt_text + Colors.RESET, end="")
        user_input = input().strip().lower()
        
        if is_numeric:
            try:
                return float(user_input)
            except ValueError:
                print(Colors.ERROR + "Please enter a valid number." + Colors.RESET)
        elif valid_options:
            if user_input in valid_options:
                return user_input
            else:
                options_str = ", ".join(valid_options)
                print(Colors.ERROR + f"Please enter a valid option from: {options_str}" + Colors.RESET)
        else:
            return user_input


def length_converter():
    """Performs length unit conversions"""
    print(Colors.TITLE + "\n--- LENGTH CONVERTER ---" + Colors.RESET)
    
    conversion_factors = {
        "mm": 0.001,   # 1 mm = 0.001 m
        "cm": 0.01,    # 1 cm = 0.01 m
        "m": 1,        # 1 m = 1 m
        "km": 1000,    # 1 km = 1000 m
        "in": 0.0254,  # 1 in = 0.0254 m
        "ft": 0.3048,  # 1 ft = 0.3048 m
        "yd": 0.9144,  # 1 yd = 0.9144 m
        "mi": 1609.34  # 1 mi = 1609.34 m
    }
    
    valid_units = list(conversion_factors.keys())
    
    # Gets source unit
    unit_from = get_valid_input(
        f"Enter the source unit ({'/'.join(valid_units)}): ", 
        valid_options=valid_units
    )
    
    # Gets target unit (ensure it's different)
    while True:
        unit_to = get_valid_input(
            f"Enter the target unit ({'/'.join(valid_units)}): ", 
            valid_options=valid_units
        )
        if unit_from != unit_to:
            break
        print(Colors.ERROR + "Please choose a different unit for conversion." + Colors.RESET)
    
    # Get value to convert
    value = get_valid_input(f"Enter the value in {unit_from}: ", is_numeric=True)
    
    value_in_meters = value * conversion_factors[unit_from]
    converted_value = value_in_meters / conversion_factors[unit_to]
    
    # Display result
    print(Colors.SEPARATOR + "─" * 50 + Colors.RESET)
    print(Colors.RESULT + f"{value:.2f} {unit_from} = {converted_value:.2f} {unit_to}" + Colors.RESET)
    print(Colors.SEPARATOR + "─" * 50 + Colors.RESET)


def weight_converter():
    """Performs weight unit conversions"""
    print(Colors.TITLE + "\n--- WEIGHT CONVERTER ---" + Colors.RESET)
    
    conversion_factors = {
        "mg": 0.001,        # 1 mg = 0.001 g
        "g": 1,             # 1 g = 1 g
        "kg": 1000,         # 1 kg = 1000 g
        "oz": 28.3495,      # 1 oz = 28.3495 g
        "lb": 453.592       # 1 lb = 453.592 g
    }
    
    valid_units = list(conversion_factors.keys())
    
    # Get source unit
    unit_from = get_valid_input(
        f"Enter the source unit ({'/'.join(valid_units)}): ", 
        valid_options=valid_units
    )
    
    # Get target unit (ensure it's different)
    while True:
        unit_to = get_valid_input(
            f"Enter the target unit ({'/'.join(valid_units)}): ", 
            valid_options=valid_units
        )
        if unit_from != unit_to:
            break
        print(Colors.ERROR + "Please choose a different unit for conversion." + Colors.RESET)
    
    # Get value to convert
    value = get_valid_input(f"Enter the value in {unit_from}: ", is_numeric=True)
    
    # Perform conversion
    value_in_grams = value * conversion_factors[unit_from]
    converted_value = value_in_grams / conversion_factors[unit_to]
    
    # Display result
    print(Colors.SEPARATOR + "─" * 50 + Colors.RESET)
    print(Colors.RESULT + f"{value:.2f} {unit_from} = {converted_value:.2f} {unit_to}" + Colors.RESET)
    print(Colors.SEPARATOR + "─" * 50 + Colors.RESET)


def temperature_converter():
    """Performs temperature unit conversions"""
    print(Colors.TITLE + "\n--- TEMPERATURE CONVERTER ---" + Colors.RESET)
    
    valid_units = ["c", "f", "k"]
    
    # Get source unit
    unit_from = get_valid_input(
        "Enter the source unit (c/f/k): ", 
        valid_options=valid_units
    )
    
    while True:
        unit_to = get_valid_input(
            "Enter the target unit (c/f/k): ", 
            valid_options=valid_units
        )
        if unit_from != unit_to:
            break
        print(Colors.ERROR + "Please choose a different unit for conversion." + Colors.RESET)
    
    # Get value to convert
    value = get_valid_input(f"Enter the value in {unit_from.upper()}: ", is_numeric=True)
    
    # Converts value to Celsius 
    if unit_from == "c":
        celsius = value
    elif unit_from == "f":
        celsius = (value - 32) * 5 / 9
    else: 
        celsius = value - 273.15
    
    # Converts from Celsius to target unit
    if unit_to == "c":
        result = celsius
    elif unit_to == "f":
        result = (celsius * 9 / 5) + 32
    else:  
        result = celsius + 273.15
    
    print(Colors.SEPARATOR + "─" * 50 + Colors.RESET)
    print(Colors.RESULT + f"{value:.2f} °{unit_from.upper()} = {result:.2f} °{unit_to.upper()}" + Colors.RESET)
    print(Colors.SEPARATOR + "─" * 50 + Colors.RESET)


def main_menu():
    """Main menu"""
    while True:
        print_header()
        
        print(Colors.BRIGHT_WHITE + "Select conversion type:" + Colors.RESET)
        print(f"{Colors.BRIGHT_CYAN}1.{Colors.RESET} Length")
        print(f"{Colors.BRIGHT_CYAN}2.{Colors.RESET} Weight")
        print(f"{Colors.BRIGHT_CYAN}3.{Colors.RESET} Temperature")
        print(f"{Colors.BRIGHT_CYAN}4.{Colors.RESET} Exit")
        
        choice = get_valid_input("Enter your choice (1-4): ", valid_options=["1", "2", "3", "4"])
        
        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        else: 
            print(Colors.SUCCESS + "\nThank you for using the Unit Converter! Goodbye." + Colors.RESET)
            break
        
        # Ask if the user wants to continue
        continue_choice = get_valid_input("\nDo you want to perform another conversion? (y/n): ", 
                                         valid_options=["y", "n", "yes", "no"])
        if continue_choice in ["n", "no"]:
            print(Colors.SUCCESS + "\nThank you for using the Unit Converter! Goodbye." + Colors.RESET)
            break


if __name__ == "__main__":
    main_menu()