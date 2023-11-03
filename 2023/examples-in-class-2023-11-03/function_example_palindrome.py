def is_palindrome(value):
    reverse = value[::-1]
    if value == reverse:
        print(f"{value} is a palindrome")
    else:
        print(f"{value} is NOT a palindrome")

is_palindrome("atilla")
is_palindrome("hannah")
is_palindrome("efe")
is_palindrome("1221")

from_user = input("please enter a string to check if it is a palindrome: ")
is_palindrome(from_user)