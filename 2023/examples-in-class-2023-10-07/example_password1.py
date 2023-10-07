import random
import string

r1 = random.randint(0,len(string.ascii_letters)-1)
s1 = string.ascii_letters[r1]

r2 = random.randint(0,len(string.ascii_letters)-1)
s2 = string.ascii_letters[r2]

r3 = random.randint(0,len(string.ascii_letters)-1)
s3 = string.ascii_letters[r3]
r4 = random.randint(0,len(string.ascii_letters)-1)
s4 = string.ascii_letters[r4]
r5 = random.randint(0,len(string.ascii_letters)-1)
s5 = string.ascii_letters[r5]

password  = s1 + s2 + s3 + s4 + s5
print(password)