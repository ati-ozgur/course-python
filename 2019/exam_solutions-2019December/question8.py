import string
import random as rnd
def random_password(length = 12):
    password = ""
    max = len(string.ascii_uppercase)    
    for index in range(length):
        random_num = rnd.randint(1,max-1)
        random_char = string.ascii_uppercase[random_num]
        password = password + random_char

    return password

for u in range(1000):
    p1 = random_password()
    print(p1)
