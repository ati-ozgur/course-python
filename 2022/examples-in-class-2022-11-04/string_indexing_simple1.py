name = "Jacobs University"
name_list = ["J","a","c","o","b","s"," ","U","n","i","v","e","r","s","i","t","y"]

print(name)

print(name[0])
print(name_list[0])


print(name[1])
print(name_list[1])

print(name[10])
print(name_list[10])

## C, C#, java

size = len(name)
# I will get an exception since I am starting count from 0
# print(f"last element {name[size]}")

print(f"last element is {name[size-1]}")
print(f"last second element is {name[size-2]}")

## pythonic way

print(f"last element is {name[-1]}")
print(f"last second element is {name[-2]}")




