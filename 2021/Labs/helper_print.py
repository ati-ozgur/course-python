def print_lists(list_of_lists):
	for liste1 in list_of_lists:
		for var in liste1:
			print(var)

if __name__ == "__main__":
	l = [["*"], ["**"], ["***"], ["****"], ["*****"]]
	print_lists(l)
