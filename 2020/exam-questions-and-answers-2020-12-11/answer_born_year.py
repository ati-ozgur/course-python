from datetime import datetime
today = datetime.today()
#print(today)
#year = int(str(today)[0:4])
year = today.year
#print(year)
print("please enter your age:")
age = int(input())
born_year = year - age

#print(f"hello, you were born in {born_year}")
print("hello, you were born in",born_year)