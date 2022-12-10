
l1 = list(range(100))
new_list = []
for num in l1:
	if num % 7 == 0:
		new_list = new_list + [num] 

 # list comprehension is here filter numbers divisible by 7

print(l1)
print(new_list)
print(sum(new_list))