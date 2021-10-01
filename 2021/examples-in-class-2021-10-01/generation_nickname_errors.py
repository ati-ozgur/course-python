temp = input("please enter your birth year: ")
birth_year = int(temp)


if birth_year < 1946:
    print("No nickname")
elif birth_year >= 1946 and birth_year <= 1964:
  print("Baby Boomers")
elif birth_year >= 1965 and birth_year <= 1980:
    print("Gen X")
elif birth_year >= 1981 and birth_year <= 1996:
  print("Gen Y")
elif birth_year >= 1997 and birth_year <= 2012:
    print("Gen Z")
elif birth_year > 2012:
    print("Gen A")

