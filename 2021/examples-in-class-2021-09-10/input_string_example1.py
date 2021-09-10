str_age = input("please give your age: ")
age = int(str_age)
print(age)
print(str_age)
print(age + 1)

# TypeError: can only concatenate str (not "int") to str
#print(str_age + 1)

print(str_age + "1")
