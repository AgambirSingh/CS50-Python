# Initialize an empty dictionary to store grocery items and their quantities
grocery = {}

# Infinite loop to continuously accept user input
while True:
    try:
        # Read user input, convert to uppercase, and strip any leading/trailing whitespace
        item = input().upper().strip()

        # Check if the item is not in the grocery dictionary
        if item not in grocery:
            # Initialize item's quantity in grocery
            grocery[item] = 1
        else:
            # Update item's quantity
            grocery[item] = grocery[item] + 1

    # Handle end-of-file (EOF) input, typically triggered by Ctrl+D (UNIX/Linux) or Ctrl+Z (Windows)
    except EOFError:
        # Sort the grocery dictionary by item names and store in sorted_dict
        sorted_dict = dict(sorted(list(grocery.items())))

        # Print each item and its quantity from the sorted dictionary
        for item in sorted_dict:
            print(sorted_dict[item], item, sep=" ")

        # Break the loop after printing all items
        break

    # Handle any KeyError exceptions (although this isn't required in this context)
    except KeyError:
        pass