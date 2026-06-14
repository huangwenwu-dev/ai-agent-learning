contacts = {"小明": "13800001111", "小红": "13912345678"}
contacts["小刚"] = "13888889999"
del contacts["小明"]
if "小红" in contacts:
    print(contacts["小红"])
else:
    print("不存在")
for name, phone in contacts.items():
    print(f"{name}: {phone}")

    input("按回车键退出...")