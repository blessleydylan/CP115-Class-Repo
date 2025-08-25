 # set variables and values

monthly_membership = 120
personal_training = 80
locker_rental = 25
towel_service = 15
one_time_registration_fee = 50

total_sessions = 6

 # calculation process

first_month_cost = 50 + 120 + 80 * 6 + 25 + 15
second_month_cost = 120 + 80 * 6 + 25 + 15
annual_month_cost = first_month_cost + 11 * second_month_cost

 # print output

print(first_month_cost)
print(second_month_cost)
print(annual_month_cost)