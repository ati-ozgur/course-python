
#Write a function that finds if a given string argument is Palindrome. A Palindrome string is equal to its reverse, that is its reading is the same backward as forward.
#For example: efe, hannah, ava, anna are palindromes.
#Test your function with above examples and test with at least 3 different 
# non-Palindrome examples. nixon, example, xxxzz
#You may use string functions in this function.


def is_palindrome(str_to_test):
	reverse_str = str_to_test[::-1]
	if reverse_str == str_to_test:
		return True
	else:
		return False

name_list = ["efe","hannah","ava","anna","nixon", "example", "xxxzz","xxxzzxxx"]

for name in name_list:
	if is_palindrome(name):
		print(f"{name} is a palindrome")
	else:
		print(f"{name} is not a palindrome")

