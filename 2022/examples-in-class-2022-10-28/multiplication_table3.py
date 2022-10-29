"""
  1 2 3 4  5   6
1 1 2 3 4  5  6
2 2 4 6 8 10 12
3 3 6 9 12 15 18
4 
5
6
"""
"""
1 2 3 4  5  6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30 
6 12 18 24 30 36
"""

def print_multiplication_line(index,max_num):
	for second_index in  range(1,max_num + 1):
		multiplication_result = index * second_index
		print(f"{multiplication_result}\t", end = '')
	print("")

# print_multiplication_line(1,10)
# print_multiplication_line(2,10)
# print_multiplication_line(3,10)
# print_multiplication_line(4,10)

max_num = 10
for index in range(1,max_num + 1):
	print_multiplication_line(index,max_num)