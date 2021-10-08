# Find sum(1..n) > total

total_to_find = 2000

total_current = 0

index = 0

while total_current < total_to_find:
    index  = index + 1
    total_current = total_current + index


print("1..",index," = ",total_current," > ",total_to_find)