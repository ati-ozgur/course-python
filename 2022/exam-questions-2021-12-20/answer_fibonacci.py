def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

for index in range(20):
    print(index,fibonacci(index))

F1 = fibonacci(1)
assert F1 == 1

F9 = fibonacci(9)
assert F9 == 55
F10 = fibonacci(10)
assert F10 == 89
F18 = fibonacci(18)
assert F18 == 4181