#examples_function1.py

# finding a prime?
#write a function which gives a true or false 
#if a given number is prime number
str_upper_range = input("give a number")
upper_range = int(str_upper_range)


for n in range(2, upper_range):
    for x in range(2, n):
        if n % x == 0:
             print(n, 'equals', x, '*', n//x)
             break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')









