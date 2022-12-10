l1 = []
for num in range(10):
	l1 = l1 + [num * num]

l2 = [num*num for num in range(10)]

print("l1",l1)
print("l2",l2)
