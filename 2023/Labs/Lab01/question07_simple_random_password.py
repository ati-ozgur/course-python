import random
import string


#print(string.ascii_letters)
#print(string.ascii_letters[20])

# print(random.randint(3, 9)) 

random_number1=random.randint(0, 51)
random_password_char1= string.ascii_letters[random_number1]

random_number2=random.randint(0, 51)
random_password_char2= string.ascii_letters[random_number2]

random_number3=random.randint(0, 51)
random_password_char3= string.ascii_letters[random_number3]

random_number4=random.randint(0, 51)
random_password_char4= string.ascii_letters[random_number4]


random_number5=random.randint(0, 51)
random_password_char5= string.ascii_letters[random_number5]

random_number6=random.randint(0, 51)
random_password_char6= string.ascii_letters[random_number6]

random_number7=random.randint(0, 51)
random_password_char7= string.ascii_letters[random_number7]

random_number8=random.randint(0, 51)
random_password_char8= string.ascii_letters[random_number8]


random_password = random_password_char1 + random_password_char2 + random_password_char3 + random_password_char4 + random_password_char5 + random_password_char6 + random_password_char7 + random_password_char8

print("random password is", random_password)

#print("random number", random_number1, "random_password_char1",random_password_char1)
