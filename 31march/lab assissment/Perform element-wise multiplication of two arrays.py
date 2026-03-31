import numpy as np

# Taking input from user
arr1 = np.array(list(map(int, input("Enter elements of first array: ").split())))
arr2 = np.array(list(map(int, input("Enter elements of second array: ").split())))

# Check if arrays have same shape
if arr1.shape != arr2.shape:
    print("Error: Arrays must be of the same size")
else:
    # Element-wise multiplication
    result = arr1 * arr2
    print("Element-wise multiplication:", result)