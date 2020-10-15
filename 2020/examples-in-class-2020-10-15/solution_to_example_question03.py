

#Write palindrome function again but use recursion in its definition. For example you need to work following way:
#hannah anna nn

def is_palindrome_recursive(str_to_test):
		#print("str_to_test",str_to_test)
		if len(str_to_test) < 2:
			#print("string is empty or only 1 char")
			return True

		first_char = str_to_test[0]
		last_char = str_to_test[-1]
		if first_char != last_char:
			return False
		else:
			l = len(str_to_test) -1
			new_str_to_test = str_to_test[1:l]
			return is_palindrome_recursive(new_str_to_test)




name_list = ["efe","hannah","ava","anna","nixon", "example", "xxxzz","xxxzzxxx"]

for name in name_list:
	if is_palindrome_recursive(name):
		print(f"{name} is a palindrome")
	else:
		print(f"{name} is NOT a palindrome")

