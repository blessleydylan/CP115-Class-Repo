peak_usage = float(input())
off_peak_usage = float(input())
ac_hours = int(input())
ac_temperature = int(input())
water_heater_mode = input()
lighting_hours = int(input())
oldest_appliance = int(input())
has_solar = input()
peak_percentage = float(input())

# TODO: Your code here

print(f"{total_cost:.2f}")
print(recommendation_count)
print(f"{efficiency_score}")
print(savings_potential)