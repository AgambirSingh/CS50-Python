# Main function to take input and call the convert function
def main():
    # Prompt the user to enter a word and an emoticon
    text = input("Emoticon :) or :( - ")
    # Call the convert function with the user's input
    convert(text)

# Convert function to replace emoticons with emojis
def convert(text1):
    # Replace :) with 🙂 and :( with 🙁 using nested replace functions
    print(text1.replace(":)", "🙂").replace(":(", "🙁"))

# Call the main function to execute the program
main()
