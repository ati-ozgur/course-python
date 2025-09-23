#  Python Comprehensions


## List Comprehensions



It is a way of creating lists without loops.
Comprehensions could be a more readable solution instead of loops.
Every list comprehension could be written by normal loops.

Lets start with following python loop.
This loop creates squared numbers from 0 to 9.
Resulting numbers should 0,1,4,9,...81

```python
l2 = []
for x in range(10):
    l2.append(x*x)
print(l2)
```

List comprehensions code would be:

```python
l1 = [x*x for x in range(10)]
print(l1)
```


Template for simple list comprehension is:

[expression for item in iterable]

Another interesting example.
Change a list of strings to list of integers


	str_list = ["1", "2", "3", "4", "5"]
	int_list = [int(x) for x in str_list]


As could be seen from above example, we could call functions in the comprehensions.

```python
name_list = ["atilla","aydın","duru"]

l2 = []
for name in name_list:
    l2 = l2 + [name.capitalize()]
print(l2)

l1 = [name.capitalize() for name in name_list]
print(l1)
```


### Filtering

Filtering the list is a common operation.
loop version:
	
```python
l2 = []
for x in range(10):
	if x % 3 == 1
	    l2.append(x*x)
print(l2)
```

In list comprehension, we could also filter items in the iterable with optional if

```python
l2 = [x*x for x in range(10) if x % 3 == 1]
print(l2)
```




## Double loop example

Following code creates pairs using for loop:

```python
pairs = []
for i in range(3):
    for c in ["a","b","c"]:
        pairs.append((i, c))

print(pairs)
```

Comprehension version is more compact.

```python
pairs = [(i, c) for i in range(3) for c in ["a","b","c"]]

print(pairs)
```




### Tutorials/Videos for list comprehension

- [Good blog post](https://towardsdatascience.com/11-examples-to-master-python-list-comprehensions-33c681b56212)
- [real python list comprehension tutorial](https://realpython.com/list-comprehension-python/)
- a good video tutorial: [Python Tutorial: List Comprehensions Step-By-Step
](https://youtu.be/1HlyKKiGg-4)


## Dictionary Comprehensions


## Set Comprehensions



## Links in our references

- [Python 101 book: Python Comprehensions](https://python101.pythonlibrary.org/chapter6_comprehensions.html)
- [Python tutorial: list-comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)





