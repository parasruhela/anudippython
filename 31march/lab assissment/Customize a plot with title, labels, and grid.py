import matplotlib.pyplot as plt

# Input data
x = list(map(float, input("Enter x values (space-separated): ").split()))
y = list(map(float, input("Enter y values (space-separated): ").split()))

# Check if lengths match
if len(x) != len(y):
    print("Error: x and y must have the same length")
else:
    # Create a basic line plot
    plt.plot(x, y, marker='o', linestyle='-', color='green', label='Data Line')

    # Customize title and labels
    plt.title("Customized Plot Example", fontsize=16, fontweight='bold')
    plt.xlabel("X-axis Label", fontsize=12)
    plt.ylabel("Y-axis Label", fontsize=12)

    # Add grid
    plt.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

    # Add legend
    plt.legend()

    # Show plot
    plt.show()