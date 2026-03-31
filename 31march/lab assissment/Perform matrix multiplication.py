arr = list(map(float, input("Enter array elements: ").split()))
min_val = min(arr)
max_val = max(arr)

normalized = [(x - min_val)/(max_val - min_val) for x in arr]

print("Normalized array:", normalized)