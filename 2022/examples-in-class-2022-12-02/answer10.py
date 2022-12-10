def find_digits(num):
	return [int(ch) for ch in str(num)]


print("Please enter a number to test:")
s_num = input()

digits = find_digits(s_num)


digits_reverse = digits.copy()

digits_reverse.reverse()

if digits == digits_reverse:
	print(f"Number {s_num} is a Palindrome.")
else:
	print(f"Number {s_num} is not a Palindrome.")
