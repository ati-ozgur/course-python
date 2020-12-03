# QuestionLuckyNumberSolution.py

#str_birth_year = input("please enter your birth year to find your lucky number")
str_birth_year = "1987"
print(str_birth_year)

birth_year = int(str_birth_year)
temp_birth_year = birth_year
# we know that birth year is 4 digit number

digit_1 = temp_birth_year % 10
temp_birth_year = temp_birth_year // 10
digit_10 = temp_birth_year % 10
temp_birth_year = temp_birth_year // 10
digit_100 = temp_birth_year % 10
temp_birth_year = temp_birth_year // 10
digit_1000 = temp_birth_year % 10

print("digit_1000 : ",digit_1000)
print("digit_100 : ",digit_100)
print("digit_10 : ",digit_10)
print("digit_1 : ",digit_1)

first_sum = digit_1000 + digit_100 + digit_10 + digit_1
if first_sum < 10:
    print("your lucky number is ", first_sum)
else:
    digit_1 = first_sum % 10
    first_sum = first_sum // 10
    digit_10 = first_sum % 10
    second_sum = digit_1 + digit_10
    print("your lucky number is ", second_sum)
        




