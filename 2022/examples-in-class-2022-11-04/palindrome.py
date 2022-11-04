given_string = input("please enter a string to check for palindrome: ")

reverse_string = given_string[::-1]

if given_string == reverse_string:
	print(" given string is an palindrome",given_string,reverse_string)
else:
	print(" given string is NOT an palindrome",given_string,reverse_string)
