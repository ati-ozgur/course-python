import sys

str_list_of_numbers = "10001 10002 10002 1000"
list_of_numbers = str_list_of_numbers.split(" ")
print(list_of_numbers)

min_value =  10000
max_value =  -10000

for str_n in list_of_numbers:
    n = int(str_n)
    min_value = min(min_value,n)
    max_value = max(max_value,n)


print(f"min_value: {min_value}, max_value: {max_value}")    