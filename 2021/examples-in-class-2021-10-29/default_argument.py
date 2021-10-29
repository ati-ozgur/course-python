import random
import string



def create_password(password_length= 12,contains_non_ascii = False):
    password = ""
    for i in range(password_length):
        if contains_non_ascii:
            password_char = random.choice(string.printable)
        else:
            password_char = random.choice(string.ascii_letters)
        password=password + password_char


    return password

for i in range(100):
    password = create_password()

    #password = create_password(12, contains_non_ascii=True)
    #password = create_password(5, True)
    print(i, password)
