def find_second_largest(lst):
    if len(lst) < 2:
        return None

    largest = second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and num > second_largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None


# Taking input from user
user_input = input("Enter numbers separated by space: ")
numbers = list(map(int, user_input.split()))

result = find_second_largest(numbers)

if result is None:
    print("No second largest element")
else:
    print("Second largest element is:", result)