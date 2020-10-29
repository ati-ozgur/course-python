
def find_age(p_birth_year):
   if isinstance(p_birth_year, str): 
      birth_year = int(p_birth_year)
      return 2020-birth_year - 1
   elif isinstance(p_birth_year, int): 
      return 2020-p_birth_year - 1
   else:
      print("Please give string or integer as birth year")





str_input = input("what is your birth year:")

age = find_age(str_input)

print(f"your age is {age}")


age = find_age(1980)
print(f"your age is {age}")
