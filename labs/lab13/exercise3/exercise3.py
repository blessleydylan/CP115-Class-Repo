grade = float(input())

# TODO: Your code here
while grade < 0 or grade > 100:
    print("Invalid grade. Please enter a grade between 0 and 100.")
    grade = float(input())
# Once a valid grade is entered
print(f"Valid grade entered: {grade}")


print(valid_count)
print(f"{average:.2f}")
