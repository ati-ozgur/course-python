def get_first_digit(num):
    str_num = str(num)
    str_digit = str_num[0]
    digit = int(str_digit)
    return digit

assert get_first_digit(12021) == 1
assert get_first_digit(92021) == 9
assert get_first_digit(72003443) == 7