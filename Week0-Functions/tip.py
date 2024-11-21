def main():
    # Get meal cost
    dollars = dollars_to_float(input("How much was the meal? "))
    # Get tip percentage
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # Calculate tip
    tip = dollars * percent
    # Print tip amount
    print(f"Leave ${tip:.2f}")

def dollars_to_float(cost):
    # Remove $ and convert to float
    return float(cost.strip("$"))

def percent_to_float(percent):
    # Remove % and convert to float
    return float(percent.strip("%")) / 100

# Run the program
main()
