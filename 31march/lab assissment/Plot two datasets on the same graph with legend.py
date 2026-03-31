import matplotlib.pyplot as plt

# Input first dataset
x1 = list(map(float, input("Enter x values for first dataset: ").split()))
y1 = list(map(float, input("Enter y values for first dataset: ").split()))

# Input second dataset
x2 = list(map(float, input("Enter x values for second dataset: ").split()))
y2 = list(map(float, input("Enter y values for second dataset: ").split()))

# Check if lengths match
if len(x1) != len(y1) or len(x2) != len(y2):
    print("Error: x and y values for each dataset must have the same length")
else:
    # Plot first dataset
    plt.plot(x1, y1, marker='o', linestyle='-', color='b', label='Dataset 1')

    # Plot second dataset
    plt.plot(x2, y2, marker='s', linestyle='--', color='r', label='Dataset 2')

    # Labels and title
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Two Datasets on Same Graph")
    plt.grid(True)

    # Show legend
    plt.legend()

    # Show plot
    plt.show()