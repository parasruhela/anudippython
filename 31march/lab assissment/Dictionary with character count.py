def count_characters(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq


# Taking input from user
text = input("Enter a string: ")

result = count_characters(text)
print("Character frequency:", result)