num = int(input("enter the number:"))


if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        num //= 10
        count += 1

print(count)