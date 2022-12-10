from datetime import datetime
today = datetime.today()
print(today)

current_year = today.year

print("please enter your age:")
age = input()
age = int(age)

born_year = current_year - age

print("hello, you were born in born_year",born_year)