def get_first_digit(num):
    # write your function here
    while num > 10:
        num = num // 10
    return num

assert get_first_digit(12021) == 1
assert get_first_digit(92021) == 9
assert get_first_digit(72003443) == 7