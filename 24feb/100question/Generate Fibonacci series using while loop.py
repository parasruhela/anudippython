n = int(input("enter the value:"))

a = 0
b = 1
count = 0

while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1