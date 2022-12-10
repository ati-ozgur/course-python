def find_digits(num):
	s_num = str(num)	
	l1 = []
	for ch in s_num:
		l1 = l1 + [int(ch)]
	return l1

print(find_digits(100))
print(find_digits(987))
print(find_digits(121))
print(find_digits(34543))
print(find_digits(4567))