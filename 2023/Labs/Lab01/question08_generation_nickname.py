str_birth_year = input("please enter your birth year: ")

birth_year = int(str_birth_year)

print("birth_year",birth_year)
if birth_year >= 1901 and birth_year <= 1924:
    print("your are from The Greatest Generation")
if birth_year >= 1928 and birth_year <= 1945:
    print("your are from The Silent Generation")
if birth_year >= 1946 and birth_year <= 1964:
    print("your are from Baby Boomers")
if birth_year >= 1955 and birth_year <= 1965:
    print("your are from Generation Jones")
if birth_year >= 1965 and birth_year <= 1980:
    print("your are from Generation X")
if birth_year >= 1977 and birth_year <= 1983:
    print("your are from Xennials")
if birth_year >= 1981 and birth_year <= 1996:
    print("your are from Millennials")
if birth_year >= 1997  and birth_year <= 2010:
    print("your are from Generation Z")
if birth_year >= 2011:
    print("your are from Generation Alpha")

