from datetime import datetime
today = datetime.today()

today = 2020

print("please enter your age:")
age = input()
age = int(age)

born_year = today - age

print("hello, you were born in born_year",born_year)