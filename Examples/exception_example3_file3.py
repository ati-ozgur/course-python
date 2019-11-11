file_not_read = True 
while file_not_read:
    try:
        filename = input("please write a filename: ")
        f = open(filename, "r")
        print(f.read()) 
        file_not_read = False
    except FileNotFoundError:
        print("file not found, please write another filename")
