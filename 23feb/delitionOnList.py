from doctest import OutputChecker


numbers = [34,56,8,56,4657,78]
print(numbers)
# if we have index
numbers.pop(2)
print("index 2 removed")
print(numbers)

# wen we dont have index
numbers.remove(56)
print("56 removed")
print(numbers)
