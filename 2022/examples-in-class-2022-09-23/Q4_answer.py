
print("please input your birth year")
str_birth_year = input()

birth_year = int(str_birth_year)

nickname = "No Nickname"
if birth_year >= 1997 and birth_year <= 2012:
    nickname = "Gen Z"
if birth_year >= 1981 and birth_year <= 1996:
    nickname = "Millennials"
if birth_year >= 1965 and birth_year <= 1980:
    nickname = "Gen X"
if birth_year >= 1955 and birth_year <= 1964:
    nickname = "Boomers II*"
if birth_year >= 1946 and birth_year <= 1954:
    nickname = "Boomers I*"
if birth_year >= 1928 and birth_year <= 1945:
    nickname = "Post War"
if birth_year >= 1922 and birth_year <= 1927:
    nickname = "WWII"

print(f"you have born in the {birth_year} and your nickname is {nickname}")