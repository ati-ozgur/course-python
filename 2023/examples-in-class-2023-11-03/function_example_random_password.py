import string
import random

def random_password(password_length):
    password = ""
    for _ in range(password_length):
       password = password + random.choice(string.ascii_letters) 
    
    print(password)

for _ in range(100):
    random_password(20)