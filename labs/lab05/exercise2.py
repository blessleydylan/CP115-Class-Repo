# Import the math module to access mathematical constants like pi
import math

def calculate_circle_properties():
    """
    Calculates and prints the area and circumference of a circle
    based on user input for the radius.
    """
    # Use a try-except block to handle non-numeric input gracefully
    try:
        # Prompt the user to enter the radius of the circle
        radius_str = input("Please enter the radius of the circle: ")
        
        # Convert the input string to a floating-point number
        radius = float(radius_str)

        # Check if the radius is a non-negative number
        if radius < 0:
            print("The radius cannot be a negative number. Please try again.")
            return

        # Calculate the area of the circle using the formula: Area = π * r^2
        area = math.pi * (radius ** 2)

        # Calculate the circumference of the circle using the formula: Circumference = 2 * π * r
        circumference = 2 * math.pi * radius

        # Print the results, formatted to two decimal places for better readability
        print(f"\nFor a circle with a radius of {radius}:")
        print(f"The area is: {area:.2f}")
        print(f"The circumference is: {circumference:.2f}")

    except ValueError:
        # This block will execute if the user input cannot be converted to a float
        print("Invalid input. Please enter a valid number for the radius.")

# Call the function to run the program
calculate_circle_properties()
