import inflect

names=[] #List for user to add names

while True:
    #get names from user
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError: #Press ctrl+D to stop the loop
        print()
        break

# inflect is module and .engine().join is fucntion used to add (, and) in sentences
mylist = inflect.engine().join((names))
print("Adieu, adieu, to " + mylist)