
#Write a python function that creates random password. 
#This function should have a default parameter of password_length of value 12. 
# You can use string and random module methods in this function.
import string
import random


def create_random_password(password_length=12):
	password = ""
	for index in range(password_length):
		password = password + random.choice(string.ascii_letters)

	return password

print(create_random_password())




