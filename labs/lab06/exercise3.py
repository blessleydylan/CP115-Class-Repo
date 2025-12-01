# 1. Ask the user for their name
# The input() function reads a line from input and returns a string.
student_name = input("Please enter your name: ")

# Change letters to uppercase and lowercase
uppercase_name = student_name.upper()
lowercase_name = student_name.lower()

# Print full name, uppercase name, lowercase name and name length to user
print(f"Full Name: {student_name}")
print(f"Uppercase: {uppercase_name}")
print(f"Lowercase: {lowercase_name}")
print(f"Name length: {len(student_name)}")
