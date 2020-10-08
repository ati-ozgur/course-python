def summation_even_numbers(N):
	summation = 0
	for n in range(N+1):
		if n % 2 == 0:
			summation = summation + n


	return summation


summation_even_1_to_28 = summation_even_numbers(28)
summation_even_1_to_12 = summation_even_numbers(12)
summation_even_1_to_100 = summation_even_numbers(100)

print("summation_even_1_to_28",summation_even_1_to_28)
print("summation_even_1_to_12",summation_even_1_to_12)
print("summation_even_1_to_100",summation_even_1_to_100)
