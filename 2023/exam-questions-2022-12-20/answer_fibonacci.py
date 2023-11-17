def fibonacci(n):
    # F0 = 0, F1 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        Fn =  fibonacci(n-1) + fibonacci(n-2)
        return Fn


F1 = fibonacci(1)
assert F1 == 1

F10 = fibonacci(10)
assert F10 == 55
F11 = fibonacci(11)
assert F11 == 89
F19 = fibonacci(19)
assert F19 == 4181
