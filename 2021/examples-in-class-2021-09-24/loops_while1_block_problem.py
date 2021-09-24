n = 5
index = 1
total = 0
while index <= n:
    print(index)
total = total + index
index = index + 1
# since I did not put any indentation to line 6 and 7
# line 5 runs forever (or we stop the program)
# to make it while block, the statements must be indented.

print("total",total)
