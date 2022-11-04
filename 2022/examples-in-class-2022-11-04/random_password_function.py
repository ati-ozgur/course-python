import string
import random


def create_random_password():
	random_password = ""
	for index in range(10):
		random_char = random.choice(string.ascii_letters)
		random_password = random_password + random_char

	return random_password


for index in range(100):
	password = create_random_password()
	print(password)