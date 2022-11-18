def sayHello(name,country):
    print(f"hello {name} and you are coming from {country}")


# this constructs stop following lines to be executed
# when this file is imported
# But when this file runs by itself
# following lines will executed
if __name__ == "__main__":  
    # positional calling
    sayHello("Atilla","Türkiye")

    # by keywords
    sayHello(country="Bulgaria",name="Atilla")
