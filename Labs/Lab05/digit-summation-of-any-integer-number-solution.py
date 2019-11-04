# digit-summation-of-any-integer-number.md

# entered_number = 190837523478

# summation = 1+9+0+8+3+7+5+2+3+4+7+8#  = 57

def find_summation(number, summation = 0):
    if (number > 10):
        summation = summation + number % 10
        number = number // 10
        find_summation(number,find_summation)
    else
        summation = summation + number
        print("summation is ", summation)


