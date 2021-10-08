
for index in range(1,101):
#    if index % 15 == 0:
#        print("fifteen")
    if index % 3 == 0 and index % 5 == 0 :
        print("fifteen")
    elif index % 3 == 0:
        print("three")
    elif index % 5 == 0:
        print("five")
    else:
        print(index)

