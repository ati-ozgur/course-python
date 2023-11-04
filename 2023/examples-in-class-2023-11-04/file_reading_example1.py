# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)