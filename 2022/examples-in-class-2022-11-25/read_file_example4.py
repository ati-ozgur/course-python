try:
	print("trying to open a file which DOES NOT exists")
	with open("division_example2.py", "rt") as in_file:
		text = in_file.read()
	print(text)
except FileNotFoundError:
	print("File does not exists ")

print("code continues here")