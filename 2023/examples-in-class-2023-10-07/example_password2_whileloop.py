import random
import string


max_password_length = 20
password = ""

while len(password) < max_password_length:
    r1 = random.randint(0,len(string.ascii_letters)-1)
    s1 = string.ascii_letters[r1]
    password = password + s1

print(password)