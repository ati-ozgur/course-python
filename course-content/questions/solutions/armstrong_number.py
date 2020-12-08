def check_armstrong_number(num):
	temp = num
	first = temp % 10
	temp = (temp - first) // 10
	second = temp % 10
	temp = (temp - second) // 10
	third = temp % 10

	val = (first ** 3) + (second ** 3) + (third ** 3)
	#print(third,second,first)
	return val == num


for num in range(100,1000):
	if check_armstrong_number(num):
		print(num)

#print(check_armstrong_number(371))
#print(check_armstrong_number(317))
#print(check_armstrong_number(999))
#print(check_armstrong_number(100))


