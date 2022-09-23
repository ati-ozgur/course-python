
print("please input your birth year")
str_birth_year = input()

birth_year = int(str_birth_year)


if birth_year >= 1997 and birth_year <= 2012:
    nickname = "Gen Z"
elif birth_year >= 1979 and birth_year <= 1996:
    nickname = "Millennials"
# for the year 1980 below line will not work since above elif line works
elif birth_year >= 1965 and birth_year <= 1980:
    nickname = "Gen X"
elif birth_year >= 1955 and birth_year <= 1964:
    nickname = "Boomers II*"
elif birth_year >= 1946 and birth_year <= 1954:
    nickname = "Boomers I*"
elif birth_year >= 1928 and birth_year <= 1945:
    nickname = "Post War"
elif birth_year >= 1922 and birth_year <= 1927:
    nickname = "WWII"
else:
    nickname = "No Nickname"

print(f"you have born in the {birth_year} and your nickname is {nickname}")