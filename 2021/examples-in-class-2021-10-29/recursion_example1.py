
# infinite recursive function example
# we need to do something so that
# eventually, we will escape from
# calling itself
# we have nothing, thefore we got following error
# RecursionError: maximum recursion depth exceeded while calling a Python object
def recursive_func1():
    print("recursive_func1 called")
    recursive_func1()


recursive_func1()

