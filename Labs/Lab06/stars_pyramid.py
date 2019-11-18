n = 5

index_stars = 1
index_spaces = n-1
while index_spaces >= 0:
    spaces = " "*(index_spaces)
    stars = "*" * (index_stars)
    index_spaces -=1
    index_stars +=2
    print(spaces + stars)
