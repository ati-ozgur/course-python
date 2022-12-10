from datetime import datetime
today = datetime.today().year


print("please enter your age:")
age = int(input())

born_year = today - age

print("hello, you were born in born_year",born_year)