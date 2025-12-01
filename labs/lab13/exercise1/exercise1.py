correct_password = "python123"
attempts_used = 0
login_successful = False  # Default state

while attempts_used < 3:
    password = input()
    attempts_used += 1

    if password == correct_password:
        login_successful = True
        break  # stop immediately if correct

# Print exactly what the test expects:
print('True' if login_successful else 'False')
print(str(attempts_used))
