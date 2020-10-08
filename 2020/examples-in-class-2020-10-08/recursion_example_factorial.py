

def factorial(n):
    if n == 0:
        return 1
    if n<0:
        return "Error, negative numbers do not have factorial values!!"
    return n * factorial(n - 1)

def factorial2(n):
    if n == 0:
        return 1
    elif n<0:
        return "Error, negative numbers do not have factorial values!!"
    else:
        return n * factorial2(n - 1)



fact = factorial(5)
print("factorial 5!",fact)