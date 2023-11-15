
def print_star_pyramid(num):
    max_line_length = 2*num
    n = 1
    while n <= num:
        star_count = 2 * n - 1
        line = "*" * star_count
        line = line.center(max_line_length)
        print(line)
        n = n + 1


print_star_pyramid(5)


# print(" " * 3 + "*" * (2*1-1))
# print(" " * 2 + "*" * (2*2-1))
# print(" " * 1 + "*" * (2*3-1))
# print(" " * 0 + "*" * (2*4-1))

