try:
	# we will read a file which exists
	print("trying to open a file which exists")
	with open("division_example1.py", "rt") as in_file:
		text = in_file.read()
	print(text)
except:
	print("an error occured")

print("code continues here")