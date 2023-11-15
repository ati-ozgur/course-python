# write two functions here
def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False



assert is_odd(5) 
assert is_odd(11) 
assert is_odd(19) 
assert is_odd(21) 

assert is_odd(6) == False 
assert is_odd(12) == False
assert is_odd(20) == False
assert is_odd(32) == False


assert is_even(5) == False 
assert is_even(11) == False
assert is_even(19) == False
assert is_even(21) == False

assert is_even(6) 
assert is_even(12)
assert is_even(20)
assert is_even(32)
