import sys

str_list_of_numbers = "1 12 15 21 -3 45 999 0 23"
list_of_numbers = str_list_of_numbers.split(" ")
print(list_of_numbers)

min_value =  sys.maxsize
max_value =  -sys.maxsize

for str_n in list_of_numbers:
    n = int(str_n)
    min_value = min(min_value,n)
    max_value = max(max_value,n)


print(f"min_value: {min_value}, max_value: {max_value}")    