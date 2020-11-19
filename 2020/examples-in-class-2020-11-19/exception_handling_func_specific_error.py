def print_division(a,b):
	try:
		result = a / b
		print(f"result: {result}")
	except:
		print("error occurred")




print_division(10,5)
print_division(10,0)

print_division(10,2)

str_line = input("please enter two numbers to divide:")

a = int(str_line.split(" ")[0])
b = int(str_line.split(" ")[1])

print_division(a,b)