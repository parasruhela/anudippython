# Input list of marks
marks = [85, 92, 78, 110, -5, 92, 67, 45]

# 1. Remove invalid marks (less than 0 or greater than 100)
valid_marks = [m for m in marks if 0 <= m <= 100]

if len(valid_marks) == 0:
    print("No valid marks available.")
else:
    # 2. Calculate average
    average = sum(valid_marks) / len(valid_marks)

    # 3. Find topper(s)
    highest = max(valid_marks)
    toppers = [m for m in valid_marks if m == highest]

    # 4. Assign grade based on average
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Display results
    print("Valid Marks:", valid_marks)
    print("Average:", round(average, 2))
    print("Highest Mark:", highest)
    print("Number of Toppers:", len(toppers))
    print("Grade:", grade)