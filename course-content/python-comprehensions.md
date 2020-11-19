#  Python Comprehensions


## List Comprehensions



It is a way of creating lists without loops.
Comprehensions could be a more readable solution instead of loops.



Simple example


	l1 = [x*x for x in range(10)]



Template for this example is

[expression for item in iterable]


We can also filter items in the iterable with optional if



	l1 = [x*x for x in range(10) if x % 3 == 1]
