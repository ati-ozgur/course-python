def filter_list(given_list,number_div):
	new_list = [num for num in given_list if num % number_div == 0] # write list comprehension in this line
	return new_list


l1 = list(range(100))

new_l3 = filter_list(l1,3)
print(new_l3)
print(len(new_l3))
assert len(new_l3) == 34
assert sum(new_l3) == 1683


new_l7 = filter_list(l1,7)
print(new_l7)
print(len(new_l7))

assert len(new_l7) == 15
assert sum(new_l7) == 735
