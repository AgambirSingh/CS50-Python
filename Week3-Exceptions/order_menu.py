menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0

while True:
    try:
        item=input("Item: ").title() #Using title to match user input with that of menu dict.
        price= price+ menu[item] #Add value from menu dict. if user input match with dict.
        print(f"Total: ${price:.2f}")
    except EOFError: 
        print()
        break
    except KeyError: #Incase user input dosn't match with menu 
        pass
