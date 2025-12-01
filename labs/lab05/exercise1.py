# This program gathers student information, stores it in variables, and displays the details with their data types.

# 1. Ask the user for their name, age, and course code.
# The input() function reads a line from input and returns a string.
student_name = input("Please enter your name: ")
student_age_str = input("Please enter your age: ")
course_code = input("Please enter your course code: ")

# 2. Convert the age string to an integer.
# The int() function is used to cast the string input for age to an integer data type.
student_age = int(student_age_str)

# 3. Display the student information.
# We use an f-string (formatted string literal) to easily embed variables into the output string.
print("\n--- Student Information ---")
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"Course Code: {course_code}")

# 4. Display the data types of the variables.
# The type() function returns the data type of an object.
print("\n--- Data Types ---")
print(f"Data type of 'student_name': {type(student_name)}")
print(f"Data type of 'student_age': {type(student_age)}")
print(f"Data type of 'course_code': {type(course_code)}")
