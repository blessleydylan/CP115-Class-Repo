student_gpa = float(input())
total_score = int(input())
number_extracurricular = input()
completed_interview = input()

# TODO: Your code here
if student_gpa >= 3.0:
    gpa_req = True
else:
    gpa_req = False

if total_score >= 1200:
    score_req = True
else:
    score_req = False

if int(number_extracurricular) >= 1:
    extra_req = True
else:
    extra_req = False

if completed_interview == "Yes":
    interview_req = True    
else:
    interview_req = False

if gpa_req == True and score_req == True and extra_req == True and interview_req == True:
    admission_status = "Accepted"
elif gpa_req + score_req + extra_req + interview_req == 3:
    admission_status = "Waitlisted"
else:
    admission_status = "Rejected"

print(admission_status)
