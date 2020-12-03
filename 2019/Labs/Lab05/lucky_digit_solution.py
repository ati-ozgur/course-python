# digit-summation-of-any-integer-number.md

# entered_number = 190837523478

# total = 1+9+0+8+3+7+5+2+3+4+7+8#  = 57
# Change this code so that it will find your lucky digit
def find_lucky_number(number, total = 0):
    if (number > 10):
        total = total + number % 10
        number = number // 10
        find_lucky_number(number,total)
    # Exit condition 
    else:
        total = total + number
        print("total is ", total)

find_lucky_number(1987)

