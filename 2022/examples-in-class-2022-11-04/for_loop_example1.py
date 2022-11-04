import random 


def create_random_list():
	random_list = []

	for index in range(100):
		num = random.randint(1,1000)
		random_list.append(num)

	return random_list


l1 = create_random_list()
print(l1)

# find summation of first 10 element with for loop
total = 0
for index in range(10):
	element = l1[index]
	total = total + element


print("Summation of first 10 elements of this list is",total)