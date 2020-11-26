# object oriented programming

Classes are templates to create objects.

	data
	methods (functions that belongs classes, most of the time uses data in the object)









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


## Special methods

- python classes have special methods that start and end with \_\_.
- __init__ constructor method for initializing objects
- __str__  a method when object converted to string, for example in print() function.




## override __str__ method


	class Person:

		def __init__(self,first_name,last_name):
			self.first_name = first_name
			self.last_name = last_name


	    def greeting(self):
	        return f"hello, {first_name} {last_name}"

	    def __str__():
	    	return self.greeting()



## Links References

- [Non-Programmer's Tutorial for Python 3/Intro to Object Oriented Programming in Python 3](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Intro_to_Object_Oriented_Programming_in_Python_3)
- [Classes in Python 101](https://python101.pythonlibrary.org/chapter11_classes.html)

## Video Tutorials





