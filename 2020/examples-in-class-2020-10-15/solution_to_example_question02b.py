
# Write palindrome function again but use a loop that goes for every character in the input string.

def check_palindrome(str_to_test):
		#reverse loop
		index_reverse = len(str_to_test) -1
		index_forward = 0
		index_stop = len(str_to_test) // 2 
		while index_reverse >= index_stop:
			#print(index_reverse)
			char_forward = str_to_test[index_forward]
			char_reverse = str_to_test[index_reverse]
			print("index_forward",index_forward,"char_forward:",char_forward,"index_reverse",index_reverse,"char_reverse",char_reverse)
			if char_forward != char_reverse:
				print(f"{str_to_test} is NOT a palindrome ")
				return
			index_reverse = index_reverse - 1
			index_forward = index_forward + 1



		print(f"{str_to_test} is a palindrome ")





check_palindrome("efe")
check_palindrome("hannah")
check_palindrome("hanXnah")
check_palindrome("ava")
check_palindrome("anna")
check_palindrome("nixon")
check_palindrome( "example")
check_palindrome( "xxxzz")
check_palindrome("xxxzzxxx")


