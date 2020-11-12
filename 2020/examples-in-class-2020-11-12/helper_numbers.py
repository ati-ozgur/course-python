def get_first_digit(number):
	return int(str(number)[0])


def get_last_digit(number):
	return number % 10

def remove_first_last_digit(number):
	s_number = str(number)
	s_number = s_number[1:-1]
	return s_number

assert get_first_digit(12021) == 1
assert get_first_digit(92021) == 9
assert get_first_digit(72003443) == 7


assert get_last_digit(12021) == 1
assert get_last_digit(92021) == 1
assert get_last_digit(72003443) == 3
