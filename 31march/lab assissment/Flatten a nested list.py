def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):  # If item is a list, recurse
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


# Example
nested_list = [1, [2, 3], [4, [5, 6]], 7]
result = flatten(nested_list)
print("Flattened list:", result)