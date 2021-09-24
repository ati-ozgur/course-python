def generation_nickname_function(birth_year):
    nickname = ""
    if birth_year >= 1946 and birth_year <= 1964:
        nickname = "Baby Boomers"
    elif birth_year >= 1965 and birth_year <= 1980:
        nickname = "Gen X"
    elif birth_year >= 1981 and birth_year <= 1996:
        nickname = "Gen Y"
    elif birth_year >= 1997 and birth_year <= 2012:
        nickname = "Gen Z"
    elif birth_year > 2012:
        nickname = "Gen A"
    else:
        nickname = "No nickname"
    return nickname

year = 2000
print("birth_year",year)
nickname = generation_nickname_function(year)
print("nickname",nickname)

year = 1932
print("birth_year", year)
nickname = generation_nickname_function(year)
print("nickname", nickname)
