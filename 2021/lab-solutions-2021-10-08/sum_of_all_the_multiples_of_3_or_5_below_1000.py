
def sum_of_all_the_multiples_of_3_or_5_below_num(num):
    total = 0
    index = 3
    while index < num:
        if index % 3 == 0 or index % 5 == 0:
            total = total + index

        index = index + 1

    return total 



assert sum_of_all_the_multiples_of_3_or_5_below_num(10) == 23
assert sum_of_all_the_multiples_of_3_or_5_below_num(1000) == 233168
