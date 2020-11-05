# you are doing something in the loop

# get a total number from user, find a summation of numbers 1..N which greater than equal to
#  this total number
# for example input number is 10
# 1 + 2 +3 +4 = 10
# your function will out 1..4 >= 10

# for example input number is 20
# 1 + 2 +3 +4 + 5 +6 = 21 >= 20
# 1000
# sum(1...N) > 1000

# 50
# 1+2+3+...+N >= 50
# 1 + 2 +3 +4 + 5 +6 + 7 + 8 +9 +10 = 55
def find_N(total):
	new_total = 0
	index = 0
	for index in range(total):
		new_total = new_total + index
		if total < new_total:
			break


	return index


total = 10
N = find_N(total)
print(f"total: {total} , N: {N}")

total = 20
N = find_N(total)
print(f"total: {total} , N: {N}")

total = 50
N = find_N(total)
print(f"total: {total} , N: {N}")


total = 1000
N = find_N(total)
print(f"total: {total} , N: {N}")
