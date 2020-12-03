# finding a total of number 1..n # sum(range(1,10))
# printing a line to screen
# writing a line to file
# finding a average of list of numbers

def no_argument():
    pass

def total(n):
    pass

def five():
    return 5

def find_total(n):
    total = sum(range(1,n))
    return total

def get_total(n):
    total = sum(range(1,n))
    return total

def print_total(n):
    total = sum(range(1,n))
    print(total)



def func_arguments1(x,y,z=10):
    print(" x:",x)
    print("y:",y)
    print("z:",z)
    return x + y + z

def func_arguments2(x,y,z):
    print(" x:",x)
    print("y:",y)
    print("z:",z)
    return x + y + z


def func_arguments2(x,y):
    z=10
    print(" x:",x)
    print("y:",y)
    print("z:",z)
    return x + y + z


# does not work
def func_arguments1(z=10,x,y):
    print(" x:",x)
    print("y:",y)
    print("z:",z)
    return x + y + z
