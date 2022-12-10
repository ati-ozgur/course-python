for i in range(1,101):
	if i % 2 == 0 and i % 5 !=0:
		print("two")
	elif i % 5 == 0 and i % 2 !=0:
		print("five")
	elif i % 5 == 0 and i % 2 ==0:
		print("ten")
	else:
		print(i)