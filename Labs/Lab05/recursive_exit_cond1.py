
# assume starting a is positive
def func1(a):
    print(a)
    # Exit condition, only calls itself if positive number
    if(a > 0):
        func1(a-1)



func1(10)