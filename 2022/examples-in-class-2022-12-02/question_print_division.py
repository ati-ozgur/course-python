def print_division(a,b):
	try:
		result = a / b
		print(f"result: {result}")
	except:
		print(f"Types are not compatible {type(a)} and {type(b)}, check your inputs")
	except:
		print("Zero division error occurred, check your inputs")
	else:
		print("else part:no error")


print_division("10","2")
print_division(10,0)
print_division(10,5)
print_division(10,2)

