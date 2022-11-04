import random 


def create_random_list():
	random_list = []

	for index in range(100):
		num = random.randint(1,1000)
		random_list.append(num)

	return random_list


l1 = create_random_list()
print(l1)

# how many elements you need so that summation is greater than 5000
total = 0
for index in range(len(l1)):
	element = l1[index]
	total = total + element
	# this is only run once, when loop sees the break. looping stops
	# therefore, a break statement without if is not meaningful
	break

print(f"Summation of first {index} elements of this list is {total}")

