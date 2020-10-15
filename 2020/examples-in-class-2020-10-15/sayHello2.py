
def sayHello1(name,place="Bremen"):
	print(f"hello to {name} from {place}")

# positional arguments
# optional/default value arguments
# named arguments

# positional calling , using default values
sayHello1("Atilla")
sayHello1("Duru")

# positional arguments, I need to remember exact position
sayHello1("Turkey","Atilla")

sayHello1("Nadhir","Tunisia")

# when I used named arguments, position does not matter
sayHello1(name = "Yousuf", place="Pakistan")

# when I used named arguments, position does not matter
sayHello1(place="China",name = "Xiaton")


sayHello1(place="China") # missing 1 required positional argument: 'name's
