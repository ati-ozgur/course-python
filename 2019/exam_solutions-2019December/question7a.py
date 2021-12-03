
for index in range(1,101):
    if index % 3 == 0 and index % 7 != 0:
        print('three')
    elif index % 3 != 0 and index % 7 == 0:
        print('seven')
    elif index % 3 == 0 and index % 7 == 0:
        print('twenty one')
    else:
        print(index)


