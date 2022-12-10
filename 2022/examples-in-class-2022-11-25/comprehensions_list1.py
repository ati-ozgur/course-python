l0 = [0,1,2,3,4,5,6,7,8,9]

l1 = []
for num in range(10):
	l1 = l1 + [num]

l2 = [num for num in range(10)]

print("l0",l0)
print("l1",l1)
print("l2",l2)
