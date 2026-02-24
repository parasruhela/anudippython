num = int(input("enter the value:"))

count = 0
temp = num

# Count digits
while temp > 0:
    temp //= 10
    count += 1

# Calculate sum of powers
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** count
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")