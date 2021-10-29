
# 5! = 5 * 4!
# 1! = 1
# 0! = 1
def factorial(x):
    if x == 1:
        return 1
    if x == 0:
        return 1
    
    return x * factorial(x-1)


f1 = factorial(5)
print(f1)

