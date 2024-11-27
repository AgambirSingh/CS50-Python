def main():
    # Get the fuel fraction from the check function
    fuel = check()
    # Convert the fuel fraction to  percentage and print the result
    Convert(fuel)

def check():
    while True:
        try:
            # Prompt the user to input  fraction in the form X/Y
            x, y = input("Fraction : ").split("/")
            x = int(x)  # Convert X to an integer
            y = int(y)  # Convert Y to an integer
            fraction = x / y  # Calculate the fraction
            if x > y:
                # Ensure the numerator is not greater than the denominator
                print("X should be greater than Y")
            else:
                break  # Exit the loop if the input is valid
        except ValueError:
            # Handle the case where the input is not two integers
            print("Input integer as X/Y")
        except ZeroDivisionError:
            # Handle the case where the denominator is zero
            print("Y can't be 0")
    return fraction  # Return the valid fraction

def Convert(fuel):
    # Convert the fraction to a percentage
    convert = round(fuel * 100)
    if convert <= 1:
        # If the percentage is 1% or less, print "E" for empty
        print("E")
    elif convert >= 99:
        # If the percentage is 99% or more, print "F" for full
        print("F")
    else:
        # Otherwise, print the percentage
        print(f"{convert}%")

if __name__ == "__main__":
    # Call the main function to start the program
    main()