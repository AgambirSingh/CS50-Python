import re


def main():
    print(parse(input("HTML: ")))

def parse(s):
    short = re.search(r'<iframe src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)"', s, re.IGNORECASE)
    if short:
        shareable = "https://youtu.be/"+short.group(1)
        return shareable


if __name__ == "__main__":
    main()
