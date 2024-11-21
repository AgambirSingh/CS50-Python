def main():
    # Prompt the user for a greeting, stripping leading/trailing spaces and converting to lowercase
    greet = input("Greeting: ").strip().lower()
    
    # Determine the monetary value based on the greeting
    if calc(greet) == 0:
        print("$0")
    elif calc(greet) == 20:
        print("$20")
    else:
        print("$100")

def calc(check):
    # If the greeting starts with "hello", return 0
    if check.startswith("hello"):
        return 0
    # If the greeting starts with "h" but is not "hello", return 20
    elif check[0] == "h":
        return 20
    # For all other cases, return 100
    return 100

# Call the main function to execute the program
main()
