monthly_income = int(input())
employment_status = input()
credit_rating = input()
employment_years = int(input())

# TODO: Your code here
if (monthly_income >= 3000):
    income_criteria = True
else:
    income_criteria = False
if (employment_status == "permanent" or employment_status == "contract"):
    employment_criteria = True
else:
    employment_criteria = False
if (credit_rating == "excellent" or credit_rating == "good"):
    credit_criteria = True
else:
    credit_criteria = False
if (employment_years >= 2):
    years_criteria = True
else:
    years_criteria = False

if (income_criteria + employment_criteria + credit_criteria + years_criteria) == 4:
    approval_status = "Approved"
elif (income_criteria + employment_criteria + credit_criteria + years_criteria) == 3:
    approval_status = "Conditionally Approved"
else:
    approval_status = "Rejected"

print(approval_status)