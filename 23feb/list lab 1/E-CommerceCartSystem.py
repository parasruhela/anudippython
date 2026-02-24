# List of product prices in cart
prices = [1200, 2500, 1200, 800, 1500, 2500]

# 1. Remove duplicate items
unique_prices = list(set(prices))

# Calculate total after removing duplicates
total = sum(unique_prices)

print("Unique Product Prices:", unique_prices)
print("Total before discount:", total)

# 2. Apply 10% discount if total > 5000
discount = 0
if total > 5000:
    discount = total * 0.10
    total -= discount
    print("Discount Applied (10%):", discount)
else:
    print("No discount applied.")

# 3. Add GST 18%
gst = total * 0.18
final_amount = total + gst

# 4. Display final payable amount
print("18% GST: ",gst)
print("Final Payable Amount:", final_amount)