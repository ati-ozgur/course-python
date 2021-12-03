str_N = input('Please enter a number N: ')
N = int(str_N)

index = 1
total = 0
while ( index <= N):
    if (index % 3 == 0 ):
        total = total + index
    index = index + 1

print('total',total)
