age_input = input()
age_count = 0
total_age = 0
average_age = 0

if (age_input != "done"):
    while ((int(age_input) > 0)) and ((int(age_input) <= 120)):
        age_count += 1
        total_age += int(age_input)
        age_input = input()
        if age_input == "done":
            break

average_age = total_age / age_count if age_count > 0 else 0

print(age_count)
print(total_age)
print(f"{average_age:.2f}")
