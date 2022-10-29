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

max_num = 6
index = 1
while index <= max_num:
	print("")
	second_index = 1
	while second_index <= max_num:
		multiplication_result = index * second_index
		print(f"{multiplication_result} ", end = '')
		second_index = second_index + 1
	index = index +1