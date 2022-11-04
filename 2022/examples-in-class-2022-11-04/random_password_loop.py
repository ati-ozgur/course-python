import string
import random



for index in range(100):
	random_password = ""
	for index in range(10):
		random_char = random.choice(string.ascii_letters)
		random_password = random_password + random_char
	print(random_password)