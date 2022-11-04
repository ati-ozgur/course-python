import string
import random



for index in range(10):
	rnd =  random.randint(0, len(string.ascii_letters)-1)
	random_char = string.ascii_letters[rnd]
	print(random_char, end="")
