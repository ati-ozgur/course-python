def print_rhombus2(symbol = "*" , length = 9):

	# if it is odd number 
	if length % 2 == 1:		
		# write other code here
		pass
	else:
		# raise error or return otherwise
		raise ValueError(f"length {length} should be odd number")


def print_rhombus1(symbol = "*" , length = 9):

	# if it is even number raise an error
	if length % 2 == 0:
		print(f"length {length} should be odd number")
		return

# this is the best way of writing this odd number checking
def print_rhombus(symbol = "*" , length = 9):

	# if it is even number raise an error
	if length % 2 == 0:
		raise ValueError(f"length {length} should be odd number")
	for index in range(1,length +1 ,2):
		line = symbol * index
		line = line.center(length)
		print(line)
	for index in range(length-2,0 ,-2):
		line = symbol * index
		line = line.center(length)
		print(line)


print_rhombus("+",21)