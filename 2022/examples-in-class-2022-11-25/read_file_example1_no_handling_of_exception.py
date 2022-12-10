# we are trying to read a file which DOES NOT exists
with open("test.txt", "rt") as in_file:
	text = in_file.read()
print(text)


print("code DOES NOT continue here since in line 2 an error occurs")