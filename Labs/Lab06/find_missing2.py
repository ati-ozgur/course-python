from random import sample 
numbers = sample(range(1,101),99)
#print(numbers)

total = sum(range(1,101))
missing = total - sum(numbers)
print("missing",missing)



