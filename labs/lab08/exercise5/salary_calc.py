 # obtain data

import employee_data

 # calculate total salary

total_salary = ( employee_data.basic_salary + employee_data.overtime_hours * employee_data.overtime_rate ) * 0.883 - 50 - 30
total_deduction = ( employee_data.basic_salary + (employee_data.overtime_hours * employee_data.overtime_rate) ) * 0.117 + 50 + 30
 # Display a payslip showing gross salary (basic + overtime), each deduction amount, total deductions, and net salary.

print(employee_data.basic_salary)
print(employee_data.overtime_hours * employee_data.overtime_rate)
print((employee_data.basic_salary + (employee_data.overtime_hours * employee_data.overtime_rate) ) * 0.117 )
print("50")
print("30")
print(total_deduction)
print(total_salary)