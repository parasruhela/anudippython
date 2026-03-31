def find_common(list1, list2):
    common = []

    for item in list1:
        if item in list2 and item not in common:
            common.append(item)

    return common


# Taking input from user
list1 = list(map(int, input("Enter first list elements (space-separated): ").split()))
list2 = list(map(int, input("Enter second list elements (space-separated): ").split()))

result = find_common(list1, list2)
print("Common elements:", result)