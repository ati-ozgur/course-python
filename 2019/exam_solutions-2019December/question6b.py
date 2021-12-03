str_N = input('Please enter a number N: ')
N = int(str_N)

total = 0
for  index in range(3,N+1,3):
    total = total + index
    index = index + 3

print('total',total)
