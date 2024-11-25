# Get Input from user
text = input("Input: ")

print("Output: ",end="")

# Loop to iterate over every letter in string
for letters in text:

    # Strip function to remove Vowels
    remove_ltr = letters.strip("aeiouAEIOU")
    print(remove_ltr, end="")

# Print for AESTHETICS ;)
print()