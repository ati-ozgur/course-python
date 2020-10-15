
def sayHello1(name):
	print(f"hello to {name}")


sayHello1("Atilla")
sayHello1("Duru")
sayHello1("")
#sayHello1() # TypeError: sayHello1() missing 1 required positional argument: 'name'


sayHello1(name = "Atilla")