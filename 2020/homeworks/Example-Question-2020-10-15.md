# Example Questions 2020-10-15


Python [string module](https://docs.python.org/3/library/string.html) contains some helpful functions for this lab.

We can use following code to see printable characters

	import string
	print(string.printable)
	print(string.printable[25])
	print(string.ascii_letters)
	print(string.ascii_letters[20])


Python [random module](https://docs.python.org/3/library/random.html) is also necessary.

We can use following code to get [random integers](https://www.w3schools.com/python/ref_random_randint.asp):

	import random
	print(random.randint(3, 9)) 


We can use following code to get random choice from list:

	import random
	mylist = ["Jacobs", "University", "Bremen"]
	print(random.choice(mylist)) 




1. Write a python function that creates random password. This function should have a default parameter of password_length of value 12.
You can use string and random module methods in this function.

2. Use above function to create 100 passwords.



