import random 

l1 = []

for index in range(20):
	num = random.randint(1,1000)
	l1.append(num)

print(l1)


print("7th element is",l1[7])

print("15th element is",l1[15])


print(l1[15:7:-1])
# we 15,14,13,12,11,10,9,8 elements
# we do not see 7th element since stop is not included


print(l1[:7:-1])
