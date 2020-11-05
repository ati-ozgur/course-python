import random as rnd
import string

user_count = 10
def create_password(length=12):
	#print(length)
	for index in range(user_count):
		
		password = ""
		for i in range(length):
			r_number = rnd.randint(0,len(string.ascii_uppercase)-1)
			password = password + string.ascii_uppercase[r_number]

		print(password)




create_password()

#print(create_password(8))