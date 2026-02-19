
cart_value = float(input("Enter cart value (₹): "))
membership = input("Enter membership (Silver/Gold/Platinum/None): ")
festival = input("Is it festival season? (yes/no): ")

discounts = []


if cart_value >= 10000:
    discounts.append(15)
elif cart_value >= 5000:
    discounts.append(10)

if membership == "silver":
    discounts.append(5)
elif membership == "gold":
    discounts.append(10)
elif membership == "platinum":
    discounts.append(15)


if festival == "yes":
    discounts.append(20)

if discounts:
    max_discount = max(discounts)
else:
    max_discount = 0

discount_amount = cart_value * (max_discount / 100)
final_amount = cart_value - discount_amount

print("Highest Discount Applied:", max_discount, "%")
print("Final Payable Amount: ₹", final_amount)
