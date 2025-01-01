def main():
    greet=input("Greeting: ").strip()
    if value(greet)== 0 :
        print ("$0")
    elif value(greet)== 20:
        print ("$20")
    elif value(greet)== 100:
        print ("$100")

def value(greeting):
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting[0]=="h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()