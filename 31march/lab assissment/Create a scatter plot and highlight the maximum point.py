import matplotlib.pyplot as plt

# Input data
x = list(map(float, input("Enter x values (space-separated): ").split()))
y = list(map(float, input("Enter y values (space-separated): ").split()))

# Check if lengths match
if len(x) != len(y):
    print("Error: x and y must have the same length")
else:
    # Scatter plot
    plt.scatter(x, y, color='blue', label='Data points')

    # Find index of maximum y value
    max_index = y.index(max(y))
    max_x = x[max_index]
    max_y = y[max_index]

    # Highlight maximum point
    plt.scatter(max_x, max_y, color='red', s=100, label='Maximum point')
    plt.text(max_x, max_y, f'({max_x},{max_y})', fontsize=9, ha='left', va='bottom')

    # Labels and title
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Scatter Plot with Maximum Point Highlighted")
    plt.legend()
    plt.grid(True)

    # Show plot
    plt.show()