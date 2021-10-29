

def recursive_func1(x):
	# do something
	x = x - 1
	print(x)
	if (x > 0):
		recursive_func1(x)
        
	# else do nothing, exit from function

recursive_func1(5)


