
income = float(input("Enter annual income (₹): "))
age = int(input("Enter age: "))

tax = 0

if age >= 60:
    exemption_limit = 300000
else:
    exemption_limit = 250000


if income <= exemption_limit:
    tax = 0
elif income <= 500000:
    tax = (income - exemption_limit) * 0.05
elif income <= 1000000:
    tax = (500000 - exemption_limit) * 0.05
    tax += (income - 500000) * 0.20
else:
    tax = (500000 - exemption_limit) * 0.05
    tax += (1000000 - 500000) * 0.20
    tax += (income - 1000000) * 0.30

print("Total Income Tax = ₹", tax)
