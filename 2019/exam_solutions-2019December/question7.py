
for index in range(1,101):
    if index % 3 == 0 and index % 7 == 0:
        print('twenty one')
    elif index % 3 == 0:
        print('three')
    elif index % 7 == 0:
        print('seven')
    else:
        print(index)


