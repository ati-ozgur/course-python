def is_prime(number):

	for number_to_check in range(2,number+1):
		if number % number_to_check == 0 and number != number_to_check:
			return False
		if number == number_to_check:
			return True


is_prime(7)

is_prime(10)

for n in range(1,21):
	result = is_prime(n)
	print("number",n,"is_prime",result)