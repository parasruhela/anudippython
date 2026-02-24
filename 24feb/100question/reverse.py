num = int(input())

negative = False
if num < 0:
    negative = True
    num = -num

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if negative:
    reverse = -reverse

print(reverse)