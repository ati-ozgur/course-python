def print_triangle(N):
	for i in range(0,N+1):
		index_reverse = N  - i
		line = " " * index_reverse + "*" * (2*i+1) # + str(i)
		print(line)

	for i in range(N-1,-1,-1):
		
		index_reverse = N  - i
		line = " " * index_reverse + "*" * (2*i+1) # + str(i)
		print(line)


N = 5
print_triangle(N)


