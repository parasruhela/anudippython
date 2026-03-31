import matplotlib.pyplot as plt

# Take input from user
x = list(map(float, input("Enter x values (space-separated): ").split()))
y = list(map(float, input("Enter y values (space-separated): ").split()))

# Check if lengths match
if len(x) != len(y):
    print("Error: x and y must have the same number of elements")
else:
    # Create line plot
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    
    # Add labels and title

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Line Plot of Given Values")
    plt.grid(True)
    
    # Show plot
    plt.show()