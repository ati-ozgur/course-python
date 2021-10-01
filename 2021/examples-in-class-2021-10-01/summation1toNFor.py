strN = input("Please enter a number:")
N = int(strN)

#N = 10

total = 0
for current in range(N+1):
    total = total + current
print("summation 1..",N,"is",total)
