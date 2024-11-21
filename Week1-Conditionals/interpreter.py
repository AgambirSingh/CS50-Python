def main():
    # Prompt the user to input an expression and split it into three parts: x, y, and z
    x, y, z = input("Expression: ").split()
    # Call the calculator function with the input values
    calculator(x, y, z)

def calculator(x, y, z):
    # Convert x and z to float for arithmetic operations
    x = float(x)
    z = float(z)

    # Perform the operation based on the value of y
    if y == "+":
        print(x + z)  # Addition
    elif y == "-":
        print(x - z)  # Subtraction
    elif y == "*":
        print(x * z)  # Multiplication
    elif y == "/" and z != 0:
        print(f"{(x / z):.1f}")  # Division with one decimal place, ensuring no division by zero
    else:
        print("Wrong input, Try again")  # Handle invalid input

# Call the main function to start the program
main()
