import numpy as np

# Take input from user
arr = np.array(list(map(int, input("Enter array elements (space-separated): ").split())))
value = int(input("Enter the value to compare: "))

# Find indices
indices = np.where(arr > value)[0]  # np.where returns a tuple, take [0] for array

print("Indices of elements greater than", value, ":", indices)