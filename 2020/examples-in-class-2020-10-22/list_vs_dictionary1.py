# Ask user to enter their country name.
# print out their phone code.

l_country_phone_code = ["China","86","Germany","49","Turkey","90"]


def country_name_to_phone_code_list(country_name):
	for index in range(len(l_country_phone_code)):
		if l_country_phone_code[index] == country_name:
			return l_country_phone_code[index+1]


def country_name_to_phone_code_dict(country_name):
	pass



print(country_name_to_phone_code_list("Turkey"))
print(country_name_to_phone_code_list("Germany"))
print(country_name_to_phone_code_list("China"))