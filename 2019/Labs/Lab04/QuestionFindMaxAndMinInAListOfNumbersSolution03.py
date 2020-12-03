import sys

str_list_of_numbers = "1 12 15 21 -3 45 999 0 23"
list_of_numbers = str_list_of_numbers.split(" ")
print(list_of_numbers)

min_value =  int(list_of_numbers[0])
max_value =  int(list_of_numbers[0])

for str_n in list_of_numbers:
    n = int(str_n)
    if n < min_value:
        min_value = n
    if n > max_value:
        max_value = n


print(f"min_value: {min_value}, max_value: {max_value}")    