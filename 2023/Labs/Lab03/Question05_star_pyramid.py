
def print_star_pyramid(num):
    n = 1
    while n <= num:
        star_count = 2 * n - 1
        space_count = num - n
        print(" " * space_count + "*" * star_count)
        n = n + 1


print_star_pyramid(5)


# print(" " * 3 + "*" * (2*1-1))
# print(" " * 2 + "*" * (2*2-1))
# print(" " * 1 + "*" * (2*3-1))
# print(" " * 0 + "*" * (2*4-1))

