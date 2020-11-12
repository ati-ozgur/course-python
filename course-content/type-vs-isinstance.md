# type vs isinstance


isinstance checks if a given object is an instance of a class, additionally it also checks for inheritance.

type only checks for equality of types.


a good example.


	type(True)  # bool
	type(True) == int # False 
	isinstance(True, int)  # True
	isinstance(False, int) # True



