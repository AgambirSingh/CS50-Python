# Prompt the user to input a file name, convert it to lowercase, and remove any leading/trailing whitespace
name = input("File name: ").lower().strip()

# Check the file extension and print the corresponding MIME type
if name.endswith(".gif"):
    print("image/gif")
elif name.endswith(".jpg") or name.endswith(".jpeg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
elif name.endswith(".txt"):
    print("text/plain")
elif name.endswith(".pdf"):
    print("application/pdf")
elif name.endswith(".zip"):
    print("application/zip")
else:
    # Default MIME type for unknown file extensions
    print("application/octet-stream")