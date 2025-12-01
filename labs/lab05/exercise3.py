# 1. Import the random module
# The random module is a built-in Python module used to generate random numbers.
import random

# 2. Take the student's class name from the user
# The input() function is used to get user input from the console.
# The class_name variable will store the string entered by the user.
class_name = input("Please enter the name of the class: ")

# 3. Generate a random number
# We use the randint() function from the random module to generate a random
# integer between 1 and 100, inclusive.
random_number = random.randint(1, 100)

# 4. Display the class information
# The print() function is used to display output to the console.
# We use an f-string to easily format the output with the variables.
print(f"Class Name: {class_name}")
print(f"Randomly generated number for this class: {random_number}")
