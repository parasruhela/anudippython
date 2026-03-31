# List of tuples (name, marks)
students = [("Aman", 85), ("Riya", 92), ("John", 78), ("Neha", 88)]

# Sort based on marks (second element of tuple)
sorted_list = sorted(students, key=lambda x: x[1])

print("Sorted list:", sorted_list)