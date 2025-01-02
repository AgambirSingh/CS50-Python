import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
# List of all available fonts
fonts= figlet.getFonts()

# Random font if user doesn't specify font in command line
if len(sys.argv) == 1:
    font = random.choice(fonts)

# Elif- User type font name, for eg. python figlet.py -f rectangles
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid usage")

    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")

    # Setting new font which user entered in command line
    figlet.setFont(font=sys.argv[2])

else:
    sys.exit("Invalid usage")

text=input("Input: ").strip()

print(figlet.renderText(text))
