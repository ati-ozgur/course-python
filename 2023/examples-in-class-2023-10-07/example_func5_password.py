import string
import random



def get_random_character():
    r1 = random.randint(0,len(string.ascii_letters)-1)
    s1 = string.ascii_letters[r1]
    return s1

def get_random_password():
    s1 = get_random_character()
    s2 = get_random_character()
    s3 = get_random_character()
    s4 = get_random_character()
    return s1 + s2 + s3 + s4  


password = get_random_password()

print(password)