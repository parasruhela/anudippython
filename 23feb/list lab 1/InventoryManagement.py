# Example list of product stock quantities
stock = [0, 5, 12, 8, 0, 20, 3, 15]

print("Original Stock:", stock)

# 1. Remove items with 0 stock
available_stock = [item for item in stock if item > 0]

print("After Removing 0 Stock Items:", available_stock)

# 2. Add restock (50 units) to items below 10
for i in range(len(available_stock)):
    if available_stock[i] < 10:
        available_stock[i] += 50

print("After Restocking Low Items:", available_stock)

# 3. Find total inventory count
total_inventory = sum(available_stock)

print("Total Inventory Count:", total_inventory)