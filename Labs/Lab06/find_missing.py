from random import sample 
numbers = sample(range(1,101),99)
#print(numbers)

for index in range(1,101):
    if index in numbers:
        continue
    else:
        print("missing",index)
        break

