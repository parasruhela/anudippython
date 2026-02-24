ch = input("enter Number Or Alphabate:")


if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Alphabet")
else:
    print("Special Character")