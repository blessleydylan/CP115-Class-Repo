# This program asks the user for their name, age, and course code,
# stores the information, and then displays it along with the data types.

# 1. Ask the user for input and store it in variables.
# The `input()` function returns a string, so the name and course_code
# are already the correct data type.
name = input("Please enter your name: ")
course_code = input("Please enter your course code: ")

# The age input is a string from `input()`, so we convert it to an integer
# using `int()`.
try:
    age_input = input("Please enter your age: ")
    age = int(age_input)
except ValueError:
    # Handle cases where the user enters a non-integer for age.
    print(f"Invalid input for age: '{age_input}'. Age must be a number.")
    age = None  # Set age to None to indicate invalid input

# 2. Display the collected student information.
print("\n--- Student Information ---")
if age is not None:
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course Code: {course_code}")

# 3. Display the data types of the variables.
print("\n--- Data Types ---")
print(f"The data type of 'name' is: {type(name)}")
if age is not None:
    print(f"The data type of 'age' is: {type(age)}")
print(f"The data type of 'course_code' is: {type(course_code)}")
