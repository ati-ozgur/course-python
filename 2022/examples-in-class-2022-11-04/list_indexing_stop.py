import random 

l1 = []

for index in range(20):
	num = random.randint(1,1000)
	l1.append(num)

print(l1)

print("15th element is",l1[15])


# start from 0 go to the 15th element, last element like range is not included
print(l1[:15])


# start from 0 and go to 5th element and goes to end of the list, last element like range is not included
print(l1[:5])