n = 5
for index in range(1,n+1):
    space_count = n-index
    star_count = index * 2 -1 
    line = "+" * space_count + "*" * star_count
    print(line)

