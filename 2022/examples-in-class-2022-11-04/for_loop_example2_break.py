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
for element in l1:
	total = total + element
	if total > 5000:
		break

print(f"Summation x number of elements of this list is {total}")

