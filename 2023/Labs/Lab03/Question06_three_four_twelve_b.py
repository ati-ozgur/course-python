for index in range(1,101):
    if index % 3 == 0 and index % 4 == 0:
        print("twelve")
    elif index % 3 == 0 and index % 4 != 0:
        print("three")
    elif index % 3 != 0 and index % 4 == 0:
        print("four")
    else:
        print(index)
