def first_non_repeating_char(s):
    # Step 1: Count frequency of each character
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Step 2: Find first character with frequency 1
    for char in s:
        if freq[char] == 1:
            return char

    return None  # If all characters repeat


# Taking input from user
text = input("Enter a string: ")

result = first_non_repeating_char(text)

if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")