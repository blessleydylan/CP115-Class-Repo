age = int(input())
accident_count = int(input())

# Your code here
if age < 25:
    base_premium = 2400
elif age <= 50:
    base_premium = 1800
else:
    base_premium = 2000

if accident_count == 0:
    penalty_amount = 0
elif accident_count <= 2:
    penalty_amount = 300
else:
    penalty_amount = 600

if accident_count == 0:
    discount_amount = base_premium * 0.1
else:
    discount_amount = 0

final_premium = base_premium + penalty_amount - discount_amount


print(base_premium)
print(int(final_premium))
print(discount_amount)