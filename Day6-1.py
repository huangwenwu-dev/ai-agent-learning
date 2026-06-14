import random

def play_one_round():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    while True:
        guess = int(input("才一个1~100之间的数字: "))
        attempts += 1
        if guess < secret:
            print("太小了")
        elif guess > secret:
            print("太大了")
        else:
            print(f"猜中了! 用了{attempts}次")
            return True
play_one_round()