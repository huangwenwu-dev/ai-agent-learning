import random

secret = random.randint(1, 100)
count = 0

while True:
    guess = int(input("猜一个1~100之间的数字："))
    count += 1
    if guess < secret:
        print("太小了，再试试")
    elif guess > secret:
        print("太大了，再试试")
    else:
        print(f"恭喜猜中！正确答案是{secret}，你一共猜了{count}次")
        break