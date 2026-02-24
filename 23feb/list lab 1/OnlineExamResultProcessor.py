# Example list of student scores
scores = [25, 34, 67, 45, 32, 89, 21, 40, 33, 55]

print("Original Scores:", scores)

# 1. Remove lowest 2 scores
scores.sort()                     # Sort in ascending order
updated_scores = scores[2:]       # Remove first 2 (lowest)

print("After Removing Lowest 2 Scores:", updated_scores)

# 2. Add grace marks of 5 to those scoring between 30–35
for i in range(len(updated_scores)):
    if 30 <= updated_scores[i] <= 35:
        updated_scores[i] += 5

print("After Adding Grace Marks:", updated_scores)

# 3. Count number of students passed (≥ 40)
passed_students = sum(1 for score in updated_scores if score >= 40)

print("Number of Students Passed:", passed_students)