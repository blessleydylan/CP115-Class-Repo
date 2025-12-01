import math

# A function to perform and display the calculations
def calculate_and_display_math(number):
    """
    Calculates the square root, square, cube, and sine of a given number
    and prints the results.
    """
    try:
        # --- Calculations ---
        # Calculate the square root of the number
        square_root = math.sqrt(number)
        
        # Calculate the number raised to the power of 2 (square)
        square = number ** 2
        
        # Calculate the number raised to the power of 3 (cube)
        cube = number ** 3
        
        # Calculate the sine value of the number
        # Note: The math.sin() function expects the input in radians.
        sine_value = math.sin(number)
        
        # --- Displaying the results ---
        print(f"For the number: {number}")
        print("-" * 25)  # A separator for better readability
        print(f"Square root: {square_root:.4f}")
        print(f"Square (Power of 2): {square:.4f}")
        print(f"Cube (Power of 3): {cube:.4f}")
        print(f"Sine value: {sine_value:.4f}")
        
    except ValueError as e:
        # Handle cases where math.sqrt() is called with a negative number
        print(f"Error: {e}. Cannot calculate the square root of a negative number.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Main program execution ---
if __name__ == "__main__":
    while True:
        try:
            # Prompt the user to enter a number
            user_input = input("Please enter a number: ")
            
            # Convert the input to a floating-point number
            # This allows for both integers and decimals.
            number = float(user_input)
            
            # Call the function to perform the calculations
            calculate_and_display_math(number)
            
            # Ask if the user wants to continue
            continue_choice = input("\nDo you want to calculate another number? (yes/no): ").lower()
            if continue_choice != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
                
        except ValueError:
            # Handle cases where the user's input is not a valid number
            print("Invalid input. Please enter a valid number.")
            print("Please try again.")
