# python built-in functions

Python has a number of built-in functions.
You can use these function without importing any library.
See complete list [here](https://docs.python.org/3/library/functions.html).


We will learn following functions in our course.
If you are curious read their descriptions from [python documentation](https://docs.python.org/3/library/functions.html).

- abs
- dir
- id
- input
- int
- isinstance
- issubclass
- len
- list
- map
- min
- open
- print
- range
- set
- sorted
- str
- sum
- super
- type


You can override these functions with your own but it is not recommended.
See following example.


	In [2]: abs(-2.0)                   
	In [3]: abs = 2             

	In [4]: abs(-2.0)                
	---------------------------------------------------------------------------
	TypeError                                 Traceback (most recent call last)
	<ipython-input-4-8449d55e35d8> in <module>
	----> 1 abs(-2.0)

	TypeError: 'int' object is not callable


## How to remember them built in function names

You do not have to remember names of the built in functions, you may always look at them from python documentation or your python itself.
If we write following in the interactive shell, we should see a big list. 
All of the lowercase names in this list are built in functions.
Try and see it.

	dir(__builtins__)
