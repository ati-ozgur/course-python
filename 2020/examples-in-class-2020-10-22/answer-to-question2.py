
#Write a python function that creates random password. 
#This function should have a default parameter of password_length of value 12. 
# You can use string and random module methods in this function.
import string
import random


def create_random_password(password_length=12):
	length = len(string.ascii_letters) - 1

	password = ""
	for index in range(password_length):
		random_number = random.randint(0, length)
		password = password +string.ascii_letters[random_number]


	return password

for index in range(100):
	print(create_random_password())




