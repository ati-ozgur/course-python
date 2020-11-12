def factorial(n):
	if n > 1:
		#call itself
		print(f"call itself {n}*{n-1}!")
		return n * factorial(n-1)
	else:
		return 1 # exit condition




#print(factorial(0)) # by definition should be 1 
#print(factorial(1))  # by definition should be 1 
#print(factorial(2))
#print(factorial(3))
#print(factorial(4))
print(factorial(5))


