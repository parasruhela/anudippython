# Example list of employee salaries
salaries = [25000, 52000, 48000, 75000, 30000, 90000, 15000, 60000]

# Define minimum wage
minimum_wage = 20000

# 1. Remove salaries below minimum wage
valid_salaries = [salary for salary in salaries if salary >= minimum_wage]

# 2. Add 5% bonus to employees with salary > 50000
updated_salaries = []
for salary in valid_salaries:
    if salary > 50000:
        salary += salary * 0.05
    updated_salaries.append(salary)

# 3. Sort salaries in descending order
updated_salaries.sort(reverse=True)

# 4. Display top 3 highest salaries
top_3 = updated_salaries[:3]

print("Valid Salaries:", valid_salaries)
print("Salaries After Bonus:", updated_salaries)
print("Top 3 Highest Salaries:", top_3)