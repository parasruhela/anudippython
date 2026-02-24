# Example list of daily temperatures (°C)
temperatures = [32, 45, 41, 38, 47, 29, 50, 42, 36, 44, 39, 46]

print("Daily Temperatures:", temperatures)

# 1. Find hottest and coldest day
hottest = max(temperatures)
coldest = min(temperatures)

print("Hottest Temperature:", hottest, "°C")
print("Coldest Temperature:", coldest, "°C")

# 2. Replace temperatures above 45°C with "Heat Alert"
updated_temperatures = temperatures.copy()

for i in range(len(updated_temperatures)):
    if updated_temperatures[i] > 45:
        updated_temperatures[i] = "Heat Alert"

print("Updated Temperatures:", updated_temperatures)

# 3. Count number of extreme days (> 40°C)
extreme_days = sum(1 for temp in temperatures if temp > 40)

print("Number of Extreme Days (> 40°C):", extreme_days)