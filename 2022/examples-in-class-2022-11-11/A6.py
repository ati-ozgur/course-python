#str_N = input("enter a number")
#N = int(str_N)
N = 10


def answer_range(N):
	total = 0
	for i in range(3,N+1,3):
		total = total + i
	return total



def answer_forloop(N):
	total = 0
	for i in range(N+1):
		if i % 3 == 0:
			total = total + i
	return total



