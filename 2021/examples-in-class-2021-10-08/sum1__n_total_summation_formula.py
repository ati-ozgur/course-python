# Find sum(1..n) > total

total_to_find = 2000

summation = int(n* (n+1) / 2)
n* (n+1) / 2 > total_to_find

n * (n+1) > 2*total_to_find
(n-1) ~= sqrt(2*total_to_find)


total_current = 0

index = 0

while total_current < total_to_find:
    index  = index + 1
    total_current = total_current + index


print("1..",index," = ",total_current," > ",total_to_find)