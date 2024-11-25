# Get user input
camelCase= input("camelCase: ")

# Print snake_case
print ("snake_case: ", end="")

# Loop/iterate through each letter
for letters in camelCase:

    # Check if any letter is upper case
    if letters.isupper():
        #convert to snake_case
       print ("_" + letters.lower(), end=(""))

    # Otherwise print letter (not required)
    else:
        print(letters, end="")

#Print space in end for AESTHETIC ;)
print()