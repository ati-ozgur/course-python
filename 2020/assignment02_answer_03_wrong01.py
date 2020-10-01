
# No fifteen in this code
for index in range(1,101):

	if index % 3 == 0:
		print("three")
	elif index % 5 == 0:
		print("five")
	elif index % 15 == 0:
		print("fifteen")
	else:
		print(index)
