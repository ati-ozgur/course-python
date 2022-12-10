# we are trying to read a file which DOES NOT exists
try:
	print("trying to open test.txt")
	with open("test.txt", "rt") as in_file:
		text = in_file.read()
	print(text)
except:
	print("an error occured")


print("code continues here")