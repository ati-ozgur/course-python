str1 = input("please enter an integer number N")

n1 = int(str1)

foo = 1

zoo = 1
while zoo <= n1:
    foo = foo * zoo
    zoo = zoo + 1

print(f"summation of 1..{n1} is {foo}" )