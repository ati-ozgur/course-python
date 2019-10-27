str_N = input("Please enter a number to find summation of 1..N: ")
N = int(str_N) + 1
total = 0
for n in range(1,N):
    total = total + n

print(total)
