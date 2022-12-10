print("please enter a number N")
s_number = input()
N = int(s_number)

print(N)

total = 0

for index in range(N+1):
	if index % 3 == 0:
		total = total + index

print(f"total of numbers up to {N} which are divisible by 3 is {total}")