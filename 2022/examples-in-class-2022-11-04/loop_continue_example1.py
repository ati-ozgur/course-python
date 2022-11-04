
customer_list = ["Bremen","Hamburg","Berlin","Düsseldorf","Köln","Duisburg"]


for customer in customer_list:
	# check that it is obey the condition
	first_char = customer[0]
	if first_char != "B":
		continue



	print("sending email to",customer)