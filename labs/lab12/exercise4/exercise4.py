score_input = input()
passing_count = 0
failing_count = 0
pass_rate = 0.0

while (score_input != "end"):
    if (int(score_input) >= 0) and (int(score_input) <= 100) and (int(score_input) >= 60):
            passing_count += 1
            score_input = input()
            if score_input == "end":
                break
    else:
            failing_count += 1
            score_input = input()
            if score_input == "end":
                break

pass_rate = (passing_count / (passing_count + failing_count) * 100) if (passing_count + failing_count) > 0 else 0.0







print(passing_count)
print(failing_count)
print(f"{pass_rate:.2f}")
