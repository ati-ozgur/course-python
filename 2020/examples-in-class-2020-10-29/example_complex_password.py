# Sample Question 3

# A complex password should satisfy following conditions

# - At least 9 characters long
# - At least contains 1 upper case and 1 lower case character
# - At least contains 1 number
# - At least contains 1 character from following special character list "!#$%&()*+,-./:;<=>?@[\]^_{|}"

password = input("Please enter a complex password example:")


if len(password) <= 9:
	print("your password should be at least 9 characters long")
else:
	print("Your password satisfies requirement of at least 9 characters long")

