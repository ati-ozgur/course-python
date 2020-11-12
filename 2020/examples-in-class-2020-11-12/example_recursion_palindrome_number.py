import helper_numbers

def palindrome_number(number):
	if helper_numbers.get_first_digit(number) != helper_numbers.get_last_digit(number):
		return False
	else:
		s_number = helper_numbers.remove_first_last_digit(number)
		if s_number == "":
			return True
		else:
			number = int(s_number)
			return palindrome_number(number)

#12021
#202
#0

# 12021 IS a palindrome_number 
# 202 IS a palindrome_number
# 4320234 IS a palindrome_number

# 12027 IS NOT a palindrome_number

print(palindrome_number(12021))
print(palindrome_number(202))
print(palindrome_number(4320234))

print(palindrome_number(12027))

#print(helper_numbers.get_first_digit(12021))
#print(helper_numbers.get_first_digit(77021))
#print(helper_numbers.get_first_digit(9021))


#print(helper_numbers.get_last_digit(12021))
#print(helper_numbers.get_last_digit(77025))
#print(helper_numbers.get_last_digit(9028))
