# loop intuition
## repeating something

Repeating something is the most easy loop.
For example, writing your name 4 times in the screen.

	Atilla
	Atilla
	Atilla
	Atilla

We can accomplish above with loops in the python, while or for loops.
We will see how they work.	


## increasing numbers

This is again very common loop type.
For example, printing out numbers from 1 to 10.
This requirement could be accomplished with while or for loops again.




## summation number 1..N


We want to find find summation of 1..10.


	1 = 1
	1+2 = 3
	1+2+3 = 6
	1+2+3+4 = 10
	1+2+3+4+5 = 15
	1+2+3+4+5+6  = 21
	1+2+3+4+5+6+7 = 28
	1+2+3+4+5+6+7+8 = 36
	1+2+3+4+5+6+7+8+9  = 45
	1+2+3+4+5+6+7+8+9+10 = 55



	 1       = 1
	(1)  + 2 = 3
	(3)  + 3 = 6
	(6)  + 4 = 10
	(10) + 5 = 15
	(15) + 6 = 21
	(21) + 7 = 28
	(28) + 8 = 36
	(36) + 9 = 45
	(45) +10 = 55


If we write this in python code.

	index = 1
	total = 0
	while index <= 10:
		total = total + index
		index = index + 1

	print(total)



change it so that it works with 1..N

	index = 1
	last_number = 10
	total = 0
	while index <= last_number:
		total = total + index
		index = index + 1

	print(total)
