from datetime import datetime
today = datetime.today()


print("please enter your age:")
age = input()
born_year = today - age

print("hello, you were born in born_year")