# Original dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Swapping keys and values
swapped_dict = {value: key for key, value in my_dict.items()}

print("Original dictionary:", my_dict)
print("Swapped dictionary:", swapped_dict)