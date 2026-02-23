age = int(input("Enter patient age: "))
heart_rate = int(input("Enter heart rate (bpm): "))
severe_injury = input("Severe injury? (yes/no): ").lower()
condition = input("Condition level (moderate/normal): ").lower()

# Check if heart rate is abnormal
if heart_rate < 60 or heart_rate > 100 or severe_injury == "yes":
    category = "Critical"

elif condition == "moderate":
    if age > 65:
        category = "Critical"  # Upgrade priority
    else:
        category = "Moderate"

else:
    category = "Normal"

print("Triage Category:", category)