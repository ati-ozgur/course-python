print("please enter an number greater than 2,")
N_str = input()

N = int(N_str)

def write_one_line(multiplication,N):
	for index in range(1,N+1):
		val = index * multiplication
		print(val, end=" ")
	print("")

for index in range(1,N+1):
	write_one_line(index,N)


