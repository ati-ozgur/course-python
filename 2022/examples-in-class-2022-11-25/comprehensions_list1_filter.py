l1 = []
for num in range(10):
	if num % 2 == 0:
		l1 = l1 + [num]

l2_nofilter = [num for num in range(10)]

l2 = [num for num in range(10) if num % 2 == 0]

print("l1",l1)
print("l2",l2)
