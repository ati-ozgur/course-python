# Python Basic Data Types

- Numbers
    - integers
    - floating point numbers
    - complex numbers
- strings
- boolean

## Find variable class name or type

use type function.

	In [6]: a = 5

	In [7]: type(a)
	Out[7]: int


## Converting between types

use object changing functions.

    int
    float
    bool
    str
    complex


## + operator works with same types


	In [8]: print("hello" + " world")
	hello world

	In [9]: print(10+1)
	11

	In [10]: print(10 + "8")
	---------------------------------------------------------------------------
	TypeError                                 Traceback (most recent call last)
	<ipython-input-10-38035139b14a> in <module>
	----> 1 print(10 + "8")

	TypeError: unsupported operand type(s) for +: 'int' and 'str'

	In [11]: print("hello" + 10)
	---------------------------------------------------------------------------
	TypeError                                 Traceback (most recent call last)
	<ipython-input-11-9d2092f62421> in <module>
	----> 1 print("hello" + 10)

	TypeError: can only concatenate str (not "int") to str


How to solve this problem? Change their types using object changing functions.



	In [12]: print(10 + int("8"))
	18

	In [13]: print("hello" + str(10))
	hello10



## Links References


- [Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)

- 


## Video Tutorials

- https://youtu.be/gCCVsvgR2KU

