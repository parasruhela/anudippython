import numpy as np

# Taking input from user (space-separated numbers)
arr = np.array(list(map(float, input("Enter array elements separated by space: ").split())))

# Calculations
mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev = np.std(arr)

# Output
print("Mean:", mean_val)
print("Median:", median_val)
print("Standard Deviation:", std_dev)