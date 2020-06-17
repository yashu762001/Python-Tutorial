def fun1(x):
    return fun2(x)

def fun2(y):
    y = y**2
    return fun3(y)

def fun3(z):
    print("hello world")
    return z+2

print(fun1(7))