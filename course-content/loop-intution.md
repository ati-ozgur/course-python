# summation number 1..N


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



	1 = 1
	1+2 = 3
	(3)+3 = 6
	(6) + 4 = 10
	(10) + 5 = 15
	((10) + 6  = 21
	(21) = 28
	(36) = 36
	(36)+9  = 45
	(36)+9+10 = 55


If we write this in python code.

	index = 1
	total = 0
	while index < 10:
		total = total + index
		index = index + 1

	print(total)



change it so that it works with 1..N

	index = 1
	last_number = 10
	total = 0
	while index < last_number:
		total = total + index
		index = index + 1

	print(total)
