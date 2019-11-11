from random import sample 
numbers = sample(range(1,101),100)
print(numbers)

def find_indices_total(l,start,stop):
    # your code here
    total = 0
    for index in range(start,stop):
        total = total + l[index]
    return total


total = find_indices_total(numbers,0,3)
print(total)