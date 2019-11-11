from random import sample 
numbers = sample(range(1,101),100)
print(numbers)

def find_indices_total(l,start,stop):
    # your code here
    total = sum(l[start:stop])
    return total


total = find_indices_total(numbers,0,3)
print(total)