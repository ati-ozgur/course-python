import random as rnd
import string

def create_password(length=12):
	#print(length)
	password = ""
	for i in range(length):
		r_number = rnd.randint(0,len(string.ascii_uppercase)-1)
		password = password + string.ascii_uppercase[r_number]

	return password


user_count = 10

for index in range(user_count):
	print(create_password())



#print(create_password(8))