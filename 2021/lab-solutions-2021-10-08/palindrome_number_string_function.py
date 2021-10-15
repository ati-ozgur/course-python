
def is_palindrome_number(value):
    value = str(value)
    # list indexing
    # string indexing
    # range(start,end,increment)
    reversed = value[::-1]
    if reversed == value:
        return True
    else:
        return False


assert is_palindrome_number(121)
assert is_palindrome_number(3443)
assert is_palindrome_number(34543)
    
assert not is_palindrome_number(321)
assert not is_palindrome_number(4567)
assert not is_palindrome_number(123421)







