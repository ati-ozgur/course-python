def sayHello(name):
	print(f"hello {name}")


# this one replaces (re-defines) above function definition
def sayHello(name,lastname):
	print(f"hello {name} {lastname}")

# this does not work since our definition is changed
sayHello("Jacobs University")


sayHello("Atilla","Ögzür")