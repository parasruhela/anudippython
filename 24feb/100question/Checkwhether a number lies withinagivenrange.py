num = float(input("enter the number:"))
lower = float(input("enter the lowest range:"))
upper = float(input("enter the greatest range:"))

if lower <= num <= upper:
    print("Within Range")
else:
    print("Out of Range")