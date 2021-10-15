
def digit_summation(num):
    value = str(num)
    total = 0
    for ch in value:
        digit = int(ch)
        total = total + digit

    return total


assert digit_summation(123) == 6

assert digit_summation(190837523478) == 57

