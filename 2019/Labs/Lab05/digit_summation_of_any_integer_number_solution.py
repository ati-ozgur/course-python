# digit-summation-of-any-integer-number.md

# entered_number = 190837523478

# total = 1+9+0+8+3+7+5+2+3+4+7+8#  = 57

def find_total(number, total = 0):
    if (number > 10):
        total = total + number % 10
        number = number // 10
        return find_total(number,total)
    # Exit condition 
    else:
        total = total + number
        return total
## Only runs if it is a main script
## if it is imported by other python files
# , it will not run
if __name__ == "__main__":
    total = find_total(1111)
    print("total is ", total)

