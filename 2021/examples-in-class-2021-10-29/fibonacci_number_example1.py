
# https://en.wikipedia.org/wiki/Fibonacci_number
def fibonacci_number(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    Fn = fibonacci_number(n-1) + fibonacci_number(n-2)
    return Fn


f5 = fibonacci_number(5)
print(f5)


f10 = fibonacci_number(10)
print(f10)
