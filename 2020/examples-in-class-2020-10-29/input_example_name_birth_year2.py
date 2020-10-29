str_input = input("what is your name and your birth year, with a space:")

#print(str_input)

l_input = str_input.split(" ")
name = l_input[0]
str_year = l_input[1]

year = int(str_year)

age = 2020-year-1


print(f"hello {name}, your age is {age}")

