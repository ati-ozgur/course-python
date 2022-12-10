def capitalize(name):
	return name[0].upper() + name[1:]
list_of_names = ["atilla","ardalan","nicholas","melissa","keni","roshanak"]
# [expression for item in iterable]

l2 = [name[0].upper() + name[1:] for name in list_of_names]
print(l2)


l3 = [ capitalize(name)  for name in list_of_names]
print(l3)

l4 = [ len(name)  for name in list_of_names]
print(l4)
	