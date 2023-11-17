import string
import random as rnd

# print(string.ascii_uppercase)
# print(rnd.randint(1, 10))


def random_password(password_length=12):
    password = ""
    for index in range(password_length):
        num = rnd.randint(0, 25)
        random_char = string.ascii_uppercase[num]
        password = password + random_char

    return password


for user_count in range(1000):
    password = random_password()
    print(password)
