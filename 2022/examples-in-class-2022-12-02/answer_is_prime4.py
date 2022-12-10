def is_prime(number):
	is_prime(10)

	for d in range(2,number):
		if number % d == 0:
			return False

	return True


for n in range(1,21):
	result = is_prime(n)
	print("number",n,"is_prime",result)