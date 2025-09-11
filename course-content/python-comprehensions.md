#  Python Comprehensions


## List Comprehensions



It is a way of creating lists without loops.
Comprehensions could be a more readable solution instead of loops.



Simple example


	l1 = [x*x for x in range(10)]



Template for this example is

[expression for item in iterable]


We can also filter items in the iterable with optional if



	l2 = [x*x for x in range(10) if x % 3 == 1]

Another interesting example.
Change a list of strings to list of integers


	str_list = ["1", "2", "3", "4", "5"]
	int_list = [int(x) for x in str_list]


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





