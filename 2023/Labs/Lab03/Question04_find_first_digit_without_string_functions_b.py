import math

def get_first_digit(num):
    return num // 10**math.floor(math.log10(num))

assert get_first_digit(12021) == 1
assert get_first_digit(92021) == 9
assert get_first_digit(72003443) == 7