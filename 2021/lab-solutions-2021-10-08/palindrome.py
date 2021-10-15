# Please write a code that finds if given input is a palindrome. 
# For example: efe, hannah, ava, anna are palindromes. 
# Test your code with above examples 
# and test with at least 3 different non-Palindrome examples. 
# nixon, example, xxxzz For our purposes space and 
# whitespace characters are distinct characters; 
# therefore, "taco cat" is not a palindrome.

def is_palindrome(value):
    # list indexing
    # string indexing
    # range(start,end,increment)
    reversed = value[::-1]
    if reversed == value:
        return True
    else:
        return False


assert is_palindrome("efe")

assert is_palindrome("efe") == True
assert is_palindrome("hannah") == True
assert is_palindrome("ava") == True
assert is_palindrome("tacocat") == True

assert not is_palindrome("nixon") 

assert is_palindrome("nixon") == False
assert is_palindrome("example") == False
assert is_palindrome("xxxzz") == False
assert is_palindrome("taco cat") == False

