def find_digits(num):
	l1 = []
	while num > 0:
		remainder = num % 10
		num = num // 10
		l1 = [remainder] + l1
	return l1



print(find_digits(100))
print(find_digits(987))
print(find_digits(121))
print(find_digits(34543))
print(find_digits(4567))