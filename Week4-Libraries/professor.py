import random


def main():

    level=get_level()
    score=0
    for _ in range(10):
        a,b=generate_integer(level)
        guess=0

        while guess <= 4:
            guess+=1

            try:
                que=int(input(f"{a} + {b} = "))
            except ValueError:
                print("Write an integer")

            if que==(a+b):
                score+=1
                guess=0
                break
            elif guess <=2:
                print("EEE")
            else:
                print(f"{a} + {b} = " , a+b)
                guess=0
                break
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            #print(f"Entered level: {level}")  # Debugging line
            if 1 <= level <= 3:
                #print("Breaking out of loop")
                return level
            else:
                print("Please enter a level between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_integer(level):
    if level == 1:
        a = random.randint(0,9)
        b = random.randint(0,9)
        return a,b
    elif level == 2:
        a = random.randint(10,99)
        b = random.randint(10,99)
        return a,b
    else:
        a = random.randint(100,999)
        b = random.randint(100,999)
        return a,b

if __name__ == "__main__":
    main()
