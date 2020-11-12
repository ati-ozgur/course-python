def factorial(n):
	fact = 1
	for index in range(n,1,-1):
		fact = fact * index
	return fact


print(factorial(0)) # by definition should be 1 
print(factorial(1))  # by definition should be 1 
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

