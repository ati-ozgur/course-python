for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print("fifteen")
    if x % 3 == 0 and x % 5 != 0:
        print("three")
    if x % 3 != 0 and x % 5 == 0:
        print("five")    
    if x % 3 != 0 and x % 5 != 0:
        print(x)

