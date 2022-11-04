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
for index in range(len(l1)):
	element = l1[index]
	# I do not want to total if it is less than 500
	if element < 500:
		continue
	total = total + element


print("Summation of elements which are higher than 500 in this list is",total)