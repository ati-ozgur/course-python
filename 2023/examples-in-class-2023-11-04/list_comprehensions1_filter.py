l2 = []
for x in range(10):
    if x % 3 == 1:
        l2 = l2 +  [x*x]
print(l2)


l1 = [x*x for x in range(10) if x % 3 == 1]
print(l1)

