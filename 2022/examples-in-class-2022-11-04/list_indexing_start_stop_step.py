import random 

l1 = []

for index in range(20):
	num = random.randint(1,1000)
	l1.append(num)

print(l1)


print("7th element is",l1[7])

print("15th element is",l1[15])


# start from 7 go to the 15th element, last element like range is not included
print(l1[7:15:4])
# 7,11,15 with increments but stop here 15 is not included
# 7,11


# start from 2 and go to 5th element and goes to end of the list, last element like range is not included
print(l1[2:5:2])
# 2,4,
