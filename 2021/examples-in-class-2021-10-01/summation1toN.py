strN = input("Please enter a number:")
N = int(strN)
#N = 10

current = 1
total = 0
while current <= N:
    total = total + current
    #print(current, total)
    current = current + 1

print("total",total)
