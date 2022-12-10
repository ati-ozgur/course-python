def find_digits(num):
	return [int(ch) for ch in str(num)]


print("Please enter a number to test:")
s_num = input()

digits = find_digits(s_num)

for start_index in range(len(digits)):
	end_index = len(digits) - start_index -1
	start_num = digits[start_index]
	end_num = digits[end_index]
	if start_num != end_num:
		print(f"Number {s_num} is not a Palindrome.")
		break

else:
	print(f"Number {s_num} is a Palindrome.")


