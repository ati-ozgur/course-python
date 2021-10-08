#str_N = input("Please enter number: ")
#N = int(str_N)
N  = 5

index = 1
while index <= N:
    space_count = N - index
    spaces = " " * space_count
    star_count = index * 2 -1
    stars = "*" * star_count
    line = spaces + stars
    print(line)
    index = index + 1