import digit_summation_of_any_integer_number_solution as d
entered_number = 1987

total = d.find_total(entered_number)
if total > 10:
    total = d.find_total(total)

print("lucky number ",total)
