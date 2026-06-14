def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(2, 3)   # 控制台会打印 5，x 值为 None
y = add_return(2, 3)  # 控制台无打印，y 值为 5

print("x =", x)   # None
print("y =", y)   # 