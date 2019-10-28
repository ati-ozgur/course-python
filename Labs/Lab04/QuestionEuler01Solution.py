
end = 1000
total = 0
for x in range(1,end):
    if x % 15 == 0:
        total = total + x
        print(x)
    elif x % 5 == 0:
        total = total + x
        print(x)
    elif x % 3 == 0:
        total = total + x
        print(x)

print(f"total = {total}")