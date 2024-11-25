# Set Variable with fixed cost
amount_due = 50

# Promt user to insert coin until required amount is met
while amount_due > 0:

    print("Amount Due:" , amount_due)

    amount = int(input("Insert Coin: "))

    # Validate Coins inserted is 25,10 or 5
    if amount in [25,10,5]:

        amount_due -= amount

        # Method 1 - If statement to Return change
        #if amount_due <= 0:
           # change = 0 - amount_due
           # print("Change Owned: " , change)

# Method 2 to Return change
change= abs(amount_due)
print("Change Owed:", change)