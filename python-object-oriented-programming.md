# object oriented programming


everything is python is an object.
To find a methods of an object use dir function

	type("")
	dir("")


	type("")
	dir(1)





# define new classes


## minimal example

	class Person:
		pass




## constructor

	class Person:

		def __init__(self,first_name,last_name):
			self.first_name = first_name
			self.last_name = last_name




## instance method

	class Person:

		def __init__(self,first_name,last_name):
			self.first_name = first_name
			self.last_name = last_name


	    def greeting(self):
	        return f"hello, {self.first_name} {self.last_name}"




## override __str__ method


	class Person:

		def __init__(self,first_name,last_name):
			self.first_name = first_name
			self.last_name = last_name


	    def greeting(self):
	        return f"hello, {first_name} {last_name}"

	    def __str__():
	    	return self.greeting()

