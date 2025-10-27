grade = float(input())
valid_count = 0
total_count = 0.0

while grade != -1:  # keep reading until a negative number
    if 0 <= grade <= 100:  # only process valid grades
        valid_count += 1
        total_count += grade
    grade = float(input())

# Calculate average safely
average = total_count / valid_count if valid_count > 0 else 0.0

print(valid_count)
print(f"{average:.2f}")
