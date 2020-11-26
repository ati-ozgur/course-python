l1 = list(range(10))

new_list = []
for x in l1:
	y = x*x
	if x % 3 == 1:
		new_list.append(y)


print(l1)
print(new_list)
