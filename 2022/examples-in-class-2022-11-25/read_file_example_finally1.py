try:
	# we will read a file which exists
	print("trying to open a file which exists")
	with open("division_example1.py", "rt") as in_file:
		text = in_file.read()
	print(text)
except:
	print("an error occured")
finally:
	print("finally lines work for both possibilities")
	print("if an error occurs, finally lines run")
	print("if an error DOES NOT occur, finally lines run")



print("code continues here")