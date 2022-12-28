def func_arguments1(x=10,y=10,z=10):
    print("x:",x)
    print("y:",y)
    print("z:",z)
    return (x + y) * z


x = 5
y = 10
z = 20

ans1 = func_arguments1(x,y,z)
assert ans1 == 300


ans2 = func_arguments1(x,y,4)
assert ans2 == 60

ans3 = func_arguments1(x)
assert ans3 == 150


ans4 = func_arguments1(10)
assert ans4 == 200

ans4 = func_arguments1(x = 20,y =30, z= 20)
assert ans4 == 1000

ans5 = func_arguments1(x = x,y =y)
assert ans5 == 150

ans6 = func_arguments1()
assert ans6 == 200
