# functions in Python

Python has built-in functions like str, print and input.
But we can also define our own functions like below.

```python
def say_hello(name):
	print("hello " + name)
```




Here def keyword is used to define function.
Among the parenthesizes, we define function arguments.
Here only one argument exists that is name.
After closing parentheses, we use double column : to finish defining line of function.
In python whitespace is important; therefore, after double column, we need to put some whitespace for function code lines.

We can use our defined functions normally.

```python
def say_hello(name):
   print("hello " + name)


say_hello("Atilla")
#hello Atilla

say_hello("Duru")
#hello Duru

```



## Example with more parameters


## Example with default parameters


## Functions returning values


if a function does not return anything, it by default returns none.
For example

```python
def say_hello(name):
   print("hello " + name)
   
ret = say_hello("atilla")
print(ret)
#hello atilla
#None
```


Since say_hello function do not use return keyword, it returns python special type None.


## Swap example

```python
a = 2
b = 4

def swap(a, b):
    temp = a
    a = b
    b = temp
swap(a, b)
print(a, b)

```



## Links in our references

- [Non-Programmer's Tutorial for Python 3/Defining Functions](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Defining_Functions)

- [Non-Programmer's Tutorial for Python 3/Advanced Functions Example](https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3/Advanced_Functions_Example)

- [Functions in Python 101](https://python101.pythonlibrary.org/chapter10_functions.html)

- [Python Functions in w3schools.com](https://www.w3schools.com/python/python_functions.asp)

## Video Tutorials

