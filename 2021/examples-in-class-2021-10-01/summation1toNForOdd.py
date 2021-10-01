strN = input("Please enter a number:")
N = int(strN)

#N = 10

total = 0
for current in range(N+1):
    if current % 2 == 1:
        total = total + current
print("summation 1..",N," for odd numbers is",total)
