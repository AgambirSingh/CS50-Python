import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        search = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
        check=0
        for n in range(1,5):
            if int(search.group(n))<256:
                check+=1

        if check == 4:
            return True
        else:
            return False
    except AttributeError:
        return False

if __name__ == "__main__":
    main()
