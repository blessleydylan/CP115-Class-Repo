# This program takes three test scores, calculates the total and average, and displays the results.

# --- Input Section ---
# Use the input() function to get a score from the user.
# The input() function returns a string, so we convert it to a float
# to allow for decimal values and to perform calculations.
print("Please enter three test scores.")

try:
    # Get the first test score
    score1_str = input("Enter score 1: ")
    score1 = float(score1_str)

    # Get the second test score
    score2_str = input("Enter score 2: ")
    score2 = float(score2_str)

    # Get the third test score
    score3_str = input("Enter score 3: ")
    score3 = float(score3_str)

    # --- Calculation Section ---
    # Calculate the total score by adding the three scores together.
    total_score = score1 + score2 + score3

    # Calculate the average score by dividing the total score by 3.
    average_score = total_score / 3

    # --- Output Section ---
    # Display a clear header for the results.
    print("\n--- Test Score Report ---")

    # Display the individual scores.
    print(f"Score 1: {score1}")
    print(f"Score 2: {score2}")
    print(f"Score 3: {score3}")

    # Display the total score.
    # The f-string is used for easy formatting of the output.
    print(f"\nTotal Score: {total_score}")

    # Display the average score, formatted to two decimal places for readability.
    print(f"Average Score: {average_score:.2f}")

except ValueError:
    # This block handles the case where the user enters text instead of a number.
    print("\nInvalid input. Please enter a valid number for the test scores.")

