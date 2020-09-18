# Enter birth year and print out generation nickname
# https://www.kasasa.com/articles/generations/gen-x-gen-y-gen-z
# Baby Boomers: Baby boomers were born between 1946 and 1964.

str_birth_year = input("please enter your birth year: ")
birth_year = int(str_birth_year)
print("your birth year is ",birth_year)

if birth_year >= 1946 and birth_year <= 1964:
    print("your birth year",birth_year," Hello Baby Boomer")

if birth_year > 1965  and birth_year < 1980:
    print("your birth year",birth_year," Hello Gen X")



