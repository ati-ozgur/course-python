import random 

l1 = []

for index in range(100):
	num = random.randint(1,1000)
	l1.append(num)


print(l1)

num_max = max(l1)
print("num_max in list is :",num_max)