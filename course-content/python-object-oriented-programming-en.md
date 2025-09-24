# Object oriented programming

Classes are templates to create objects.

- data
- methods (functions that belongs classes, most of the time uses data in the object)

Everything in python is an object.
To find a methods of an object use **dir** function

```python
	type("")
	dir("")


	type("")
	dir(1)
```



## Define new classes


### Minimal example

```python
class Person:
	pass
```



### constructor


```python
class Person:

	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
```



## instance method

```python
class Person:

	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name


    def greeting(self):
        return f"hello, {self.first_name} {self.last_name}"
```


## Special methods

- python classes have special methods that start and end with __.
- __init__ constructor method for initializing objects
- __str__  a method when object converted to string, for example in print() function.




## override __str__ method


```python
class Person:

	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name


	def greeting(self):
		return f"hello, {first_name} {last_name}"

	def __str__():
		return self.greeting()
```



## Links in our references

- [Non-Programmer's Tutorial for Python 3/Intro to Object Oriented Programming in Python 3](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Intro_to_Object_Oriented_Programming_in_Python_3)
- [Classes in Python 101](https://python101.pythonlibrary.org/chapter11_classes.html)
- [Python Classes and Objects in w3schools.com](https://www.w3schools.com/python/python_classes.asp)

## Video Tutorials

TODO




