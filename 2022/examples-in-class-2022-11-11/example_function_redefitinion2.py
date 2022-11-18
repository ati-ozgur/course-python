def sayHello(name):
	print(f"hello {name}")

sayHello("Jacobs University")

# this one replaces (re-defines) above function definition
def sayHello(name,lastname):
	print(f"hello {name} {lastname}")



sayHello("Atilla","Ögzür")

# but if I try to call with 1 argumant again, it will not work
#sayHello("Jacobs University")
