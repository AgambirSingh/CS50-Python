import sys
from tabulate import tabulate
import csv

if len(sys.argv)==2:
    filename = sys.argv[1]
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
else:
    sys.exit('Too few command-line arguments')

if not(filename.endswith(".csv")):
    sys.exit("Wrong file type")


try:
    with open(filename) as file:
        reader = csv.reader(file)
        print(tabulate(reader, headers="firstrow",tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")