def main():
    # Get user input, strip extra spaces, and convert to lowercase for consistent comparison
    Answer = input("What is Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    
    # Call the choices function to check if the answer is correct
    if choices(Answer):
        print("Yes")
    else:
        print("No")

def choices(Ans):
    # Check if the input matches any of the valid answers ("42", "forty-two", or "forty two")
    # Note: "42" is converted to string as input from the user is a string
    if Ans == "42" or Ans == "forty-two" or Ans == "forty two":
        return True
    else:
        return False

# Call the main function
main()

