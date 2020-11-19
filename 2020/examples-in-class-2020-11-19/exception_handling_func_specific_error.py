def print_division(a,b):
	try:
		result = a / b
		print(f"result: {result}")
	except ZeroDivisionError:
		print("Zero division error occurred, check your inputs")




print_division(10,5)
print_division(10,0)

print_division(10,2)
# since we do catch
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
# below line will give an error.
print_division("10","2")
