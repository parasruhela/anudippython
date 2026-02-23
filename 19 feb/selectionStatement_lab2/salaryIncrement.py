rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

# Base increment from performance
if rating == 5:
    increment = 12
elif rating == 4:
    increment = 9
elif rating == 3:
    increment = 6
elif rating == 2:
    increment = 3
else:
    increment = 0

# Experience bonus
if experience >= 3 and experience <= 5:
    increment += 2
elif experience >= 6 and experience <= 10:
    increment += 4
elif experience > 10:
    increment += 6

# Attendance bonus
if attendance >= 95:
    increment += 3
elif attendance >= 90:
    increment += 2
elif attendance >= 80:
    increment += 1

print("Total Salary Increment Percentage:", increment, "%")