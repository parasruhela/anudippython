def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen


# Taking input from user
numbers = list(map(int, input("Enter list elements (space-separated): ").split()))

result = remove_duplicates(numbers)
print("List after removing duplicates:", result)