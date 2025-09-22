monthly_income = int(input())
credit_score = int(input())
loan_amount = int(input())

# Your code here

max_loan_amount = monthly_income * 5
approval_status = "Approved" if monthly_income >= 4000 and credit_score >= 600 and loan_amount <= max_loan_amount else "Rejected"

if approval_status == "Approved":
    interest_rate = 3.5 if credit_score >= 700 else 5.5
else:
    interest_rate = 0.0


print(interest_rate)
print(max_loan_amount)
print(approval_status)