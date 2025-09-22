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
    discount_amount = 300
else:
    penalty_amount = 600



final_premium = base_premium + penalty_amount - discount_amount

if accident_count == 0:
    discount_amount = 0.90
    final_premium = base_premium * discount_amount


print(base_premium)
print(final_premium)
print(discount_amount)