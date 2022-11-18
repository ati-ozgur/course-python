def recursive(x):
	# do something
	x = x - 1
	print(x)
	if (x > 0):
		recursive(x)    


recursive(10)