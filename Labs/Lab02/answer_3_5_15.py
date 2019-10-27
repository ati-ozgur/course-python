# "Write a program that prints the numbers from 1 to 100. 
#  But for multiples of three print “three” instead of the number 
# and for the multiples of five print “five”. 
# For numbers which are multiples of both three and five print “fifteen”."

n = 1
while n <= 100:
    if n % 15 == 0:
        print("fifteen")
    elif n % 3 == 0:
        print("three")
    elif n % 5 == 0:
        print("five")
    else:
        print(n)
    n = n + 1


        