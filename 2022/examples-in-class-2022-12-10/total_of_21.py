
how_many_numbers = 0
digit_summation = 21

for number in range(100,1000):
	digit_1 = number % 10 
	number_copy = number // 10
	digit_10 = number_copy % 10 
	digit_100 = number_copy // 10

	check_condition = (
		(digit_1 + digit_10 + digit_100) == digit_summation 
		and (digit_1 != digit_10) 
		and (digit_10 != digit_100)
		and digit_1 != digit_100
	)
	if check_condition:
		print(number,digit_100,digit_10,digit_1)
		how_many_numbers = how_many_numbers + 1


print(f"digits are different and total digits of {digit_summation} numbers count is {how_many_numbers}")
	
