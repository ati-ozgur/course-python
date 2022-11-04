import string
import random



for index in range(10):
	random_char = random.choice(string.ascii_letters)
	print(random_char, end="")
