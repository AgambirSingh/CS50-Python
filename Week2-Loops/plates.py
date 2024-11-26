def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check if the length of the plate is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False
    
    # Check if the plate starts with at least two letters
    if not s[:2].isalpha():
        return False
    
    # Check for invalid characters (periods, spaces, punctuation)
    if not s.isalnum():
        return False
    
    # Check if numbers are in the middle or start with '0'
    for i in range(len(s)):
        if s[i].isdigit():
            if i < 2 or (i > 1 and not s[i:].isdigit()) or s[i] == '0':
                return False
            break
    
    return True

main()
