import matplotlib.pyplot as plt

# Input categories and values
categories = input("Enter categories (space-separated): ").split()
values = list(map(float, input("Enter corresponding values (space-separated): ").split()))

# Check if lengths match
if len(categories) != len(values):
    print("Error: Number of categories and values must match")
else:
    # Create pie chart
    plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)

    # Equal aspect ratio ensures pie is circular
    plt.axis('equal')
    plt.title("Percentage Distribution Pie Chart")
    plt.show()