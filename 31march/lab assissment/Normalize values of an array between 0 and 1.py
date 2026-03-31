import numpy as np

# Taking input from user
arr = np.array(list(map(float, input("Enter array elements (space-separated): ").split())))

# Min-Max Normalization
normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print("Normalized array:", normalized)