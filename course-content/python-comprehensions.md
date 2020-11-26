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


## Dictionary Comprehensions


## Set Comprehensions


### Examples

[Good blog post](https://towardsdatascience.com/11-examples-to-master-python-list-comprehensions-33c681b56212)