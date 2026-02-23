units = float(input("Enter units consumed: "))
senior = input("Are you a senior citizen? (yes/no): ").lower()

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
else:
    bill = units * 10

if senior == "yes":
    bill *= 0.90  # Apply 10% discount

print("Total Electricity Bill: ₹", bill)