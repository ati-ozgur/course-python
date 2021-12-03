str_N = input('Please enter a number N: ')
N = int(str_N)

index = 3
total = 0
while ( index <= N):
    total = total + index
    index = index + 3

print('total',total)
