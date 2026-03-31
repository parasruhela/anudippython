import numpy as np

# Taking input from user
arr = np.array(list(map(int, input("Enter array elements (space-separated): ").split())))

# Replace odd numbers with -1
arr[arr % 2 == 1] = -1

print("Modified array:", arr)
