import numpy as np

# Taking input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the elements row-wise:")
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

arr = np.array(matrix)

# Transpose
transpose = arr.T

print("Original matrix:\n", arr)
print("Transposed matrix:\n", transpose)