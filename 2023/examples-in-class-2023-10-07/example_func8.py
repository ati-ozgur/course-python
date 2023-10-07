# definition of function
def sayHello(first_name, last_name):
    print("Hello",first_name.capitalize(),last_name.capitalize())

def sayHello2(first_name, last_name):
    print(f"Hello {last_name.upper()}, {first_name.capitalize()[0]}" )


# calling the defined function
sayHello2("atilla","özgür")
sayHello2("duru","özgür")

