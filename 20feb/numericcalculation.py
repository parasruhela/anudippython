# firstway 
import product   
# second way
# from product import*

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def main():
    # try:

        print("Addition:", add(num1, num2))
        print("Subtraction:", subtract(num1, num2))

    # except ValueError:
    #     print("Please enter valid numbers only.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


main()
product.multiplication()

