import matplotlib.pyplot as plt

# Input product names and sales
products = input("Enter product names (space-separated): ").split()
sales = list(map(float, input("Enter sales corresponding to products (space-separated): ").split()))

# Check if lengths match
if len(products) != len(sales):
    print("Error: Number of products and sales must match")
else:
    # Create bar chart
    plt.bar(products, sales, color='skyblue')

    # Add labels and title
    plt.xlabel("Products")
    plt.ylabel("Sales")
    plt.title("Product Sales Bar Chart")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show plot
    plt.show()