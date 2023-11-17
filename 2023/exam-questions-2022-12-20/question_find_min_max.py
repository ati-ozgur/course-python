import random
random.seed(10)

def find_min(numbers):
	pass

def find_max(numbers):
	pass

max_number = 100
l1 = [ random.randint(0,max_number*10) for i in range(max_number) ]
print(l1)

assert max(l1) == find_max(l1)

assert min(l1) == find_min(l1)
