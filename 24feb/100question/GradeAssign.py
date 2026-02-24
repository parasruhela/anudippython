marks = int(input())

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 0:
    print("Grade F")
else:
    print("Invalid Marks")