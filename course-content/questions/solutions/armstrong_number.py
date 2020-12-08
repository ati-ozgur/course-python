def check_armstrong_number(num):
	first = num % 10
	num = (num - first) // 10
	second = num % 10
	num = (num - second) // 10
	third = num % 10

	print(third,second,first)


check_armstrong_number(371)
check_armstrong_number(999)
check_armstrong_number(100)


