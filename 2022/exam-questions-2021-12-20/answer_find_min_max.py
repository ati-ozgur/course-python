import random
random.seed(10)

def find_min(numbers):
	if len(numbers) > 0:
		minimum_number = numbers[0]
		for num in numbers:
			if num < minimum_number:
				minimum_number = num

		return minimum_number

def find_max(numbers):
	if len(numbers) > 0:
		maximum_number = numbers[0]
		for num in numbers:
			if num > maximum_number:
				maximum_number = num

		return maximum_number

max_number = 100
l1 = [ random.randint(0,max_number*10) for i in range(max_number) ]
print(l1)

assert max(l1) == find_max(l1)

assert min(l1) == find_min(l1)
