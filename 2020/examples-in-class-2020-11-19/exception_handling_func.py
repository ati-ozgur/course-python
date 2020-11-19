def print_division(a,b):
	try:
		result = a / b
		print(f"result: {result}")
	except: # It catches ALL errors
		print("error occurred")




print_division(10,5)
print_division(10,0)

print_division(10,2)

