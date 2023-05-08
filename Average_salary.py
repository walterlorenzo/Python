salary_monthly = input("Enter your monthly salary: ")
salary_monthly = float(salary_monthly)

hours_worked_per_month = input("Enter how many hours you work per month: ")
hours_worked_per_month = int(hours_worked_per_month)

salary_per_hour = salary_monthly / hours_worked_per_month

print("Your hourly salary will be {:.2f}".format(salary_per_hour))
