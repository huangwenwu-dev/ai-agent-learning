shopping_list = []

while True:
    print("\n1. 查看 2. 添加 3. 删除 4. 退出")
    choice = input("请选择: ")
    if choice == "1":
        print(shopping_list)
    elif choice == "2":
        item = input("添加什么? ")
        shopping_list.appdend(item)
    elif choice == "3":
        item = input("删除什么? ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("不在清单中")
    elif choice == "4":
        break