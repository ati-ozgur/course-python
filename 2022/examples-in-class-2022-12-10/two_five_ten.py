
def get_value(index):
	if index % 2 == 0 and index % 5 == 0:
		return "ten"
	elif index % 5 == 0:
		return "five"
	elif index % 2 == 0:
		return "two"
	else:
		return index

def two_five_ten_comprehensions():
	l1 = [get_value(index) for index in range(1,101)]
	return l1


def two_five_ten_loop():
	l1 = []
	for index in range(1,101):
		l1 = l1 + [get_value(index)]
	return l1

list_loop = two_five_ten_loop()
print(list_loop)

print("")

list_comprehensions = two_five_ten_comprehensions()
print(list_comprehensions)
