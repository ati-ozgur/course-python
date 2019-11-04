import string 
import random as rnd 

password_char_list = string.ascii_uppercase + string.ascii_lowercase

#print(string.ascii_uppercase)
#print(string.ascii_lowercase)
#print(password_char_list)

password_length = 8

password = ""

for i in range(password_length):
    password_char_index = rnd.randint(1,len(password_char_list)-1)
    password_char = password_char_list[password_char_index]
    password = password + password_char

print(f"password is {password}")


