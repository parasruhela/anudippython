a = float(input("enter angle1 :"))
b = float(input("enter angle2 :"))
c = float(input("enter angle3 :"))

# Check triangle validity
if a+b+c==180:
 if a + b <= c or b + c <= a or a + c <= b:
    print("Not a Triangle")
 elif a == b == c:
    print("Equilateral Triangle")
 elif a == b or b == c or a == c:
    print("Isosceles Triangle")
 else:
    print("Scalene Triangle")
else:
   print("angles not make any triangle")
