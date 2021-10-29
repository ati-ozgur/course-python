
def hello1(age,name="Unknown"):
    print(f"hello {name}, you are {age} years old")

# below gives error of
# SyntaxError: non-default argument follows default argument
#def hello2(name="Unknown",age):
#    print(f"hello {name}, you are {age} years old")

hello1(44,"Atilla")
hello1(8,"Duru")
hello1(9)
