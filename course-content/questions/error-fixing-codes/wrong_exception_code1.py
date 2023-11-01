def calculate(a,b):

	try:
		result = a / b
		print("result:",result)
	except Exception:
		print("Exception occured") 
	except ZeroDivisionError:
		print("ZeroDivisionError occured") 


calculate(#5,0) # should give ZeroDivisionError
calculate("1",5) # should give ValueError
calculate(1,5) # should work normally