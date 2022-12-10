
l1 = list(range(100))

#new_list0 = [num for num in l1] # list comprehension is here filter numbers divisible by 7

new_list = [num for num in l1 if num % 7 == 0] # list comprehension is here filter numbers divisible by 7

#print(l1)
#print(new_list0)
#print(new_list)
print(sum(new_list))