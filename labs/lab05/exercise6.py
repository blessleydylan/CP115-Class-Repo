# This program converts a given number of minutes into hours and remaining minutes.

def convert_minutes_to_hours(total_minutes):
    """
    Converts a total number of minutes into hours and minutes.

    Args:
        total_minutes (int): The total number of minutes to convert.

    Returns:
        tuple: A tuple containing the number of hours and the remaining minutes.
    """
    if total_minutes < 0:
        return 0, 0 # Handle negative input by returning 0 hours and 0 minutes

    # Use integer division (//) to get the number of full hours
    hours = total_minutes // 60

    # Use the modulo operator (%) to get the remaining minutes
    remaining_minutes = total_minutes % 60

    return hours, remaining_minutes


# --- Main program execution ---

try:
    # 1. Take time in minutes from the user.
    # The input() function gets user input as a string.
    minutes_input_str = input("Please enter the number of minutes: ")

    # 2. Convert the input string to an integer.
    total_minutes_int = int(minutes_input_str)

    # 3. Convert minutes to hours and remaining minutes.
    hours_output, minutes_output = convert_minutes_to_hours(total_minutes_int)

    # 4. Display the original minutes and the converted time format.
    print(f"\nOriginal minutes: {total_minutes_int}")
    print(f"Converted time: {hours_output} hours and {minutes_output} minutes")

except ValueError:
    print("Invalid input. Please enter a valid number.")

