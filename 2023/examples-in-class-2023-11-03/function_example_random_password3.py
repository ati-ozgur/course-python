import string
import random

# default value of 8 for password_length argument
def random_password(password_length=8):
    if password_length < 8:
        print("Password length should be greater than 8")
        return
    
    password = ""
    for _ in range(password_length):
       password = password + random.choice(string.ascii_letters) 
    print(password)

random_password()
random_password(12)

random_password(5)
