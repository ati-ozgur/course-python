# Python Basic Data Types

- Numbers
    - integers
    - floating point numbers
    - complex numbers
- strings
- boolean

## Find variable class name or type

use type function.

```python
In [6]: a = 5

In [7]: type(a)
Out[7]: int

```



## Converting/Casting between types

use object functions to change to different types.

    int
    float
    bool
    str
    complex


- [casting in w3schools.com](https://www.w3schools.com/python/python_casting.asp)



## + operator works with same types

```python
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
```

How to solve this problem? Change their types using object changing functions.


```python
In [12]: print(10 + int("8"))
18

In [13]: print("hello" + str(10))
hello10
```


## Links in our references


- [Python Data Types in w3schools.com](https://www.w3schools.com/python/python_datatypes.asp)

- 


## Video Tutorials

- [Data Types in Python](https://youtu.be/gCCVsvgR2KU)

