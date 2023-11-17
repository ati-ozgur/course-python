howmany = 0
for digit1 in range(10):
    for digit2 in range(10):
        for digit3 in range(10):
            if digit1 != digit2 and digit2 != digit3 and digit1 != digit3:             
                if (digit1 + digit2 + digit3) == 21:
                    howmany = howmany + 1
                    print(digit1,digit2,digit3,sep="")

print("digit howmany equal 21 and every digit is different number count is",howmany)
