name_list = ["atilla","aydın","duru"]

l2 = []
for name in name_list:
    l2 = l2 + [name.capitalize()]
print(l2)

l1 = [name.capitalize() for name in name_list]
print(l1)

