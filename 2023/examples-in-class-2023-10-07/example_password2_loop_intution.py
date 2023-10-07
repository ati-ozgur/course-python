import random
import string



password = ""

r1 = random.randint(0,len(string.ascii_letters)-1)
s1 = string.ascii_letters[r1]
password = password + s1

r2 = random.randint(0,len(string.ascii_letters)-1)
s2 = string.ascii_letters[r2]
password = password + s2

r3 = random.randint(0,len(string.ascii_letters)-1)
s3 = string.ascii_letters[r3]
password = password + s3

r4 = random.randint(0,len(string.ascii_letters)-1)
s4 = string.ascii_letters[r4]
password = password + s4

r5 = random.randint(0,len(string.ascii_letters)-1)
s5 = string.ascii_letters[r5]
password = password + s5

print(password)