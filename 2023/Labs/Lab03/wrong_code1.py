str_dividend = input'Please enter a dividend number for division: ")
str_divisor = input(Please enter a divisor number for division: ")

try:
    dividend  = float(strdividend)
    divisor = float(str_divisor)
    result = dividend / divisor
    print("division of {dividend}/{divisor}={result}")
except ValueError
    print("You have entered something which could not be converted to float")
    print("please enter a number")
except ZeroDivisionError:
    print("Please do not enter 0 for division)
except:
    print("An error has happened")

print("hello")


