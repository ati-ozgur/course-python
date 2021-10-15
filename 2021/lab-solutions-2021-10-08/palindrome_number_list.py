
def is_palindrome_number(value):
    l = []
    while value > 0:
        digit = value % 10
        value = value // 10
        l.append(digit)
    reversed = l[::-1]
    if reversed == l:
        return True
    else:
        return False


assert is_palindrome_number(121)
assert is_palindrome_number(3443)
assert is_palindrome_number(34543)
    
assert not is_palindrome_number(321)
assert not is_palindrome_number(4567)
assert not is_palindrome_number(123421)







