
l1 = list(range(100))
new_list = [i for i in l1  if i % 7 == 0] # list comprehension is here filter numbers divisible by 7

#print(l1)
#print(new_list)
print(sum(new_list))