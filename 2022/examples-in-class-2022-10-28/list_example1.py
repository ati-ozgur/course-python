l1 = [10,"Atilla", 65.7]

for item in l1:
	t = type(item)
	print(item)
	# this is normal string it prints as it is
	# curly bracelets { } has no effect
	print("item: {item} and type: {t}" )
	# this an f-string. 
	# when it prints variable between  curly bracelets { } are replace
	# with their values
	print(f"item: {item} and type: {t}" )
	# if I am not using f strings,
	# I need to concatanete + but it only works for strings
	# therefore, I need to use str to change other types to str
	print("item: "+ str(item) + "and type: " + str(t) )

