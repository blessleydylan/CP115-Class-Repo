weight = float(input())
height = float(input())
systolic_bp = int(input())
diastolic_bp = int(input())
heart_rate = int(input())
cholesterol = int(input())
age = int(input())
is_smoker = input()
exercise_hours = int(input())
family_history = input()
risk_score = 0
warning_count = 0

# TODO: Your code here
bmi = weight / (height ** 2)
if systolic_bp < 140 or diastolic_bp < 90:
    warning_count += 1 
else:
    warning_count = risk_score
if heart_rate < 60 or heart_rate > 100:
    warning_count += 1  
else:
    warning_count = warning_count
if cholesterol > 200:
    warning_count += 1
else:
    warning_count = warning_count
if age > 50:
    warning_count += 1 
else:
    warning_count = warning_count
if is_smoker == "yes":
    risk_score += 20 
else:
    risk_score = risk_score
if exercise_hours < 3:
    risk_score += 15
else:
    risk_score = risk_score
if family_history == "yes":
    risk_score += 10 
else:
    risk_score = risk_score



print(f"{bmi:.1f}")
print(warning_count)
print(f"{risk_score}")
print(priority_level)