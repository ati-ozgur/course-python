str_N = input("Please enter number: ")
N = int(str_N)
#N  = 5


for index in range(0,N):
    space_count = (N-index)
    star_count = (index * 2)+1
    spaces = (" " * space_count)
    stars = ("*" * star_count )
    line = spaces + stars 
    print(line )

