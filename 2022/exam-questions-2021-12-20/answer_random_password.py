import string
print(string.ascii_uppercase)
import random as rnd
num = rnd.randint(0,len(string.ascii_uppercase))

print(num)
print(string.ascii_uppercase[num])




def create_random_password(password_length=12):
    password = ""
    for index in range(password_length):
        num =  rnd.randint(0,len(string.ascii_uppercase)-1)
        character = string.ascii_uppercase[num]
        password = password + character
    return password

for user_number in range(1000):
    print("user",user_number,":",create_random_password())