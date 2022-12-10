def func_arguments1(x,y=10,z=10):
    print("x:",x)
    print("y:",y)
    print("z:",z)
    return x + y + z


x = 10
y = 10
z = 20

ret = func_arguments1(x,y,z)
print(ret)

ret = func_arguments1(x,y)
print(ret)

ret = func_arguments1(x)
print(ret)

ret = func_arguments1(x = x,y =y, z= z)
print(ret)

ret = func_arguments1(x = x,y =y)
print(ret)


