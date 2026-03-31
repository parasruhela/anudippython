import matplotlib.pyplot as plt

# Input dataset
data = list(map(float, input("Enter dataset values (space-separated): ").split()))

# Plot histogram
plt.hist(data, bins=10, color='skyblue', edgecolor='black')  # bins can be adjusted

# Add labels and title
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Dataset")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show plot
plt.show()