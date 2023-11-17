import string
import random as rnd

# print(string.ascii_uppercase)
# print(rnd.randint(1, 10))


def random_password(password_length=12):
    password = ""
    for index in range(password_length):
        random_char = rnd.choice(string.ascii_uppercase)
        password = password + random_char

    return password


for user_count in range(1000):
    password = random_password()
    print(password)
