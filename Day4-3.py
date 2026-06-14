correct_password = "123456"

while True:
    pwd = input("请输入密码：")
    if pwd == correct_password:
        print("登录成功")
        break
    else:
        print("密码错误，请重试")