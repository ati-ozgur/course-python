
for index in range(1,101):
    if index % 3 == 0 and index % 5 != 0 :
        print("three")
    elif index % 3 != 0 and index % 5 == 0:
        print("five")
    elif index % 3 == 0 and index % 5 == 0:
        print("fifteen")
    else:
        print(index)

