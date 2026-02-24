weight = float(input("enter weight in KG:"))   # in kilograms
height = float(input("enter height in Meters:"))   # in meters

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")