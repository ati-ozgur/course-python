# factorial examples
# 2! = 2*1!
# 3! = 3*2!
# 4! = 4*3!
# 5! = 5*4!
# 5! = 5*4*3*2*1

def factorial_recursive(number):
    if number == 1 or number == 0:
         return 1
    return number * factorial_recursive(number -1)

f5 = factorial_recursive(5)
print(f" factorial f5 or 5! = {f5}")

f11 = factorial_recursive(11)
print(f" factorial f11 or 11! = {f11}")