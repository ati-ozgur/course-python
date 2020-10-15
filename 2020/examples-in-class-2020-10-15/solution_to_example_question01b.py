
#Write a function that finds if a given string argument is Palindrome. A Palindrome string is equal to its reverse, that is its reading is the same backward as forward.
#For example: efe, hannah, ava, anna are palindromes.
#Test your function with above examples and test with at least 3 different 
# non-Palindrome examples. nixon, example, xxxzz
#You may use string functions in this function.


def check_palindrome(str_to_test):
	reverse_str = str_to_test[::-1]
	if reverse_str == str_to_test:
		print(f"{str_to_test} is a palindrome")
	else:
		print(f"{str_to_test} is NOT a palindrome")

check_palindrome("efe")
check_palindrome("hannah")
check_palindrome("ava")
check_palindrome("anna")
check_palindrome("nixon")
check_palindrome( "example")
check_palindrome( "xxxzz")
check_palindrome("xxxzzxxx")


