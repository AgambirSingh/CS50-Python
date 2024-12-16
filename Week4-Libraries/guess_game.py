import random

while True:  # While loop run until user input right value
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        continue

# Get random number btw 1 and user's input number
number = random.randint(1, level)

# Give hints and Validate answers
while True:
    try:
        guess = int(input("Guess: "))
        if guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue