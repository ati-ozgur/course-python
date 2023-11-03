# factorial examples
# 4! = 4*3*2*1
# 5! = 5*4*3*2*1


def factorial(number):
    result = 1
    for current in range(number,1,-1):
        result = result * current

    return result

f5 = factorial(5)
print(f" factorial f5 or 5! = {f5}")

f11 = factorial(11)
print(f" factorial f11 or 11! = {f11}")
