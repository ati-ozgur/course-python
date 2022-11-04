import random 

l1 = []

for index in range(20):
	num = random.randint(1,1000)
	l1.append(num)


print(l1)

print(l1[0])
print(l1[1])

print(l1[10])

## C, C#, java

size = len(l1)
# I will get an exception since I am starting count from 0
# print(f"last element {l1[size]}")

print(f"last element is {l1[size-1]}")
print(f"last second element is {l1[size-2]}")

## pythonic way

print(f"last element is {l1[-1]}")
print(f"last second element is {l1[-2]}")




