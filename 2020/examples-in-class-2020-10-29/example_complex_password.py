# Sample Question 3

# A complex password should satisfy following conditions

# - At least 9 characters long
# - At least contains 1 upper case and 1 lower case character
# - At least contains 1 number
# - At least contains 1 character from following special character list "!#$%&()*+,-./:;<=>?@[\]^_{|}"

import string

password = input("Please enter a complex password example:")


if len(password) <= 9:
	print("your password should be at least 9 characters long")
else:
	print("Your password satisfies requirement of at least 9 characters long")

any_lowercase_in_password = False
for ch_lowercase in string.ascii_lowercase:
	if ch_lowercase in password:
		any_lowercase_in_password = True
		break

if any_lowercase_in_password:
	print("Your password satisfies requirement of at least 1 lower case character")
else:
	print("your password should have at least 1 lower case character")

