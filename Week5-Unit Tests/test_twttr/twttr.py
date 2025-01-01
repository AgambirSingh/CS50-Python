def main():
    text = input("Input: ")
    print(shorten(text))

# shorten expects a str as input and returns that same str with all vowels
# (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
def shorten(word):
    string = ("")
    for letters in word:
        remove_ltr = letters.strip("aeiouAEIOU")
        string = string+remove_ltr
    return(string)


if __name__ == "__main__":
    main()