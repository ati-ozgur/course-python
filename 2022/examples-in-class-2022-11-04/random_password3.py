import string
import random


random_password_chars = random.choices(string.ascii_letters,k=10)
print(random_password_chars)

random_password = ""
for ch in random_password_chars:
	random_password = random_password + ch

print(random_password)
