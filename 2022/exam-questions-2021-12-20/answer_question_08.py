numbers_count = 0
for index in range(100,1000):
    str_index = str(index)
    digit_0 = int(str_index[2])
    digit_10 = int(str_index[1])
    digit_100 = int(str_index[0])
    total = digit_0 + digit_10 + digit_100
    if total == 21:
        if digit_0 != digit_10 and digit_10 != digit_100 and digit_0 != digit_100:
            numbers_count = numbers_count + 1
            print(index,digit_100,digit_10,digit_0,total)

print("digit total of 21 but all 3 digits are different number count:",numbers_count)