contacts = {"张三": "123456", "李四": "654321"}
name = input("请输入要查询的名字: ")
if name in contacts:
    print(f"{name}的电话是: {contacts[name]}")
else:
    print("查无此人")