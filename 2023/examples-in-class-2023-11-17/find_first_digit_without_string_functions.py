def get_first_digit(num):
    while num > 10:
        # below three lines equal to num = num // 10
        remainder = num % 10
        num = num - remainder
        num = int(num / 10)
    else:
        return num

assert get_first_digit(12021) == 1
assert get_first_digit(92021) == 9
assert get_first_digit(72003443) == 7