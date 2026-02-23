# Example attendance list (1 = Present, 0 = Absent)
attendance = [1, 1, 0, 0, 1, 0, 0, 0, 1, 1]

total_days = len(attendance)
present_days = sum(attendance)

# 1. Calculate attendance percentage
attendance_percentage = (present_days / total_days) * 100

print("Attendance Percentage:", round(attendance_percentage, 2), "%")

# 2. Identify students below 75%
if attendance_percentage < 75:
    print("Status: Below 75% attendance")
else:
    print("Status: Attendance satisfactory")

# 3. Replace consecutive absences with a warning flag
# (If two or more consecutive 0s appear, replace them with "Warning")

attendance_with_warning = attendance.copy()

for i in range(1, len(attendance)):
    if attendance[i] == 0 and attendance[i-1] == 0:
        attendance_with_warning[i] = "Warning"

print("Attendance with Warning Flags:", attendance_with_warning)