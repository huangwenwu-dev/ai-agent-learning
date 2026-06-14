age = int(input("请输入你的年龄："))

if age <= 12:
    print("儿童")
elif age <= 17:
    print("青少年")
elif age <= 35:
    print("青年")
elif age <= 55:
    print("中年")
else:
    print("老年")