
def digit_summation(num):
    total = 0
    while num > 0:    
        first_digit = num % 10
        total = total + first_digit
        num = num // 10
    return total


assert digit_summation(123) == 6

assert digit_summation(190837523478) == 57

