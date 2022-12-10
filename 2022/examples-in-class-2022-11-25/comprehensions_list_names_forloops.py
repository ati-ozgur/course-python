def capitalize(name):
	return name[0].upper() + name[1:]
list_of_names = ["atilla","ardalan","nicholas","melissa","keni","roshanak"]
# [expression for item in iterable]

l2 = [name[0].upper() + name[1:] for name in list_of_names]
print("l2",l2)

l2_forloop = []
for name in list_of_names:
	capitalized_name = name[0].upper() + name[1:]
	l2_forloop = l2_forloop + [capitalized_name]
print("l2_forloop",l2_forloop)

l3 = [ capitalize(name)  for name in list_of_names]
print("l3",l3)

l3_forloop = []
for name in list_of_names:
	l3_forloop = l3_forloop + [capitalize(name)]	
print("l3_forloop",l3_forloop)


l4 = [ len(name)  for name in list_of_names]
print("l4",l4)

l4_forloop = []
for name in list_of_names:
	l4_forloop = l4_forloop + [len(name)]

print("l4_forloop",l4_forloop)
