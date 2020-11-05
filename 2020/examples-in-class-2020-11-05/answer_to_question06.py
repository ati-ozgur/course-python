
def find_sum_div3(N):
	total = 0
	for index in range(3,N+1,3):
		#print("index",index)
		total = total+ index
	return total




str_N = input("Please give number N")
N = int(str_N)
print(find_sum_div3(N))