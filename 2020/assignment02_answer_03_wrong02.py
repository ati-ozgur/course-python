
# No multiple lines are printed for numbers divisible by 15 
for index in range(1,101):

	if index % 3 == 0:
		print("three",index)


	if index % 5 == 0:
		print("five",index)

		
	if index % 15 == 0:
		print("fifteen",index)
	else:
		print(index)
