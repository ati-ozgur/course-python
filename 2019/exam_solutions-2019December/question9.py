str_N = input('please enter a odd number for rhombus length')
N = int(str_N)


half_N = N // 2 + 1
for i in range(1,half_N):
    spaces_length = N // 2 - i + 1
    spaces = ' ' * spaces_length
    star_length = i * 2 - 1
    stars = '*' * star_length
    line = spaces + stars
    print(line)

for i in range(half_N,0,-1):
    spaces_length = N // 2 - i + 1
    spaces = ' ' * spaces_length
    star_length =  i * 2 - 1
    stars = '*' * star_length
    line = spaces + stars
    print(line)
