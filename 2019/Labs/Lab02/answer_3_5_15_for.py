# "Write a program that prints the numbers from 1 to 100. 

for n in range(1,101):
    if n % 15 == 0:
        print("fifteen")
    elif n % 3 == 0:
        print("three")
    elif n % 5 == 0:
        print("five")
    else:
        print(n)


        