x = 10

def func1():
    x = 20
    print("func1 内 x =", x )

def func2():
    global x
    x = 30
    print("func2 内 x =", x)

func1()
print("全局 x =", x)

func2()
print("全局 x =", x)