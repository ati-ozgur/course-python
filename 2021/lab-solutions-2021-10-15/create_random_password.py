import random
import string



def create_password(password_length= 12):
    password = ""
    for i in range(password_length):
        password_char = random.choice(string.ascii_letters)
        password=password + password_char


    return password

for i in range(100):
    password = create_password()
    print(i,password)
