a = int(input("enter the value1:"))
b = int(input("enter the value2:"))

i = 1
gcd = 1

while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        gcd = i
    i += 1

print(gcd)

    