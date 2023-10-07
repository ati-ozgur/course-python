str_year = input("please enter your birth year")
year = int(str_year)

if year >= 1901 and year <= 1924:
    print('The Greatest Generation')
elif year >= 1928 and year <= 1945:
    print('The Silent Generation')
elif year >= 1946 and year <= 1964:
    print('Baby Boomers')
elif year >= 1955 and year <= 1965:
    print('Generation Jones')
elif year >= 1965 and year <= 1980:
    print('Generation X ')
elif year >= 1977 and year <= 1983:
    print('Xennials')
elif year >= 1981 and year <= 1996:
    print('Millennials')
elif year >= 1997 and year <= 2010:
    print('Generation Z ')
elif year >= 2011:
    print('Generation Alpha ')
else:
    print('your generation is not defined in the table')



