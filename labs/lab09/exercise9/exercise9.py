applicant_age = int(input())
vision_test = input()
written_score = int(input())
driving_score = int(input())
medical_clearance = input()

# TODO: Your code here
if vision_test == "Pass":
    vision_passed = True
else:
    vision_passed = False
if written_score >= 80:
    written_passed = True
else:
    written_passed = False
if driving_score >= 85:
    driving_passed = True
else:
    driving_passed = False
if medical_clearance == "Pass":
    medical_passed = True
else:
    medical_passed = False

if (applicant_age >= 21 and vision_passed and written_passed and driving_passed and medical_passed):
    license_class = "Class A (Commercial)"
elif (applicant_age >= 18 and vision_passed and written_passed and driving_passed):
    license_class = "Class B (Regular)"
elif ((vision_passed + written_passed + driving_passed + medical_passed) >= 2):
    license_class = "Restricted License"
else:
    license_class = "Application Denied"

print(license_class)