def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        Fn = fibonacci(n-1) + fibonacci(n-2)
        return Fn


F10 = fibonacci(10)
print(f"F10 or fibonacci 10th numbers is {F10}")
F11 = fibonacci(11)
print(f"F11 or fibonacci 11th numbers is {F11}")
F19 = fibonacci(19)
print(f"F19 or fibonacci 19th numbers is {F19}")