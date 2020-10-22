# Ask user to enter their country name.
# print out their phone code.


l_country_phone_code2 = [("China","86"),("Germany","49"),("Turkey","90")]


def country_name_to_phone_code_list2(country_name):
	for name,code in l_country_phone_code2:
		if name == country_name:
			return code


def country_name_to_phone_code_dict(country_name):
	pass



print(country_name_to_phone_code_list2("Turkey"))
print(country_name_to_phone_code_list2("Germany"))
print(country_name_to_phone_code_list2("China"))