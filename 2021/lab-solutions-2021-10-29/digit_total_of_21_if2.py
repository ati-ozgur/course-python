count_of_numbers = 0
for d1 in range(1, 10):
    for d2 in range(1, 10):
        for d3 in range(1, 10):
            if not (d3 == d1 or d3 == d2 or d2 == d1):
                total = d1 + d2 + d3
                if total == 21:
                    count_of_numbers = count_of_numbers + 1
                    print(d1,d2,d3)

print("count_of_numbers:", count_of_numbers)
