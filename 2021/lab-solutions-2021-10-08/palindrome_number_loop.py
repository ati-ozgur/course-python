import math

def is_palindrome_number(value):
    is_palindrom = True
    while value > 0:
        size = int(math.log10(value))
        first_digit = value % 10
        last_digit = value // 10**size
        if first_digit == last_digit:
            # remove last digit
            value = value - (last_digit * 10**size)
            # remove first digit
            value = value // 10
            continue
        else:
            is_palindrom = False
            break
    return is_palindrom



assert is_palindrome_number(121)
assert is_palindrome_number(3443)
assert is_palindrome_number(34543)
    
assert not is_palindrome_number(321)
assert not is_palindrome_number(4567)
assert not is_palindrome_number(123421)







