import random

def play_one_round():
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        guess = int(input(f"猜数字（剩余{remaining}次）："))
        attempts += 1

        if guess < secret:
            print("太小了")
        elif guess > secret:
            print("太大了")
        else:
            print(f"恭喜！猜中了，用了{attempts}次")
            return True
    print(f"失败！正确答案是{secret}")
    return False 
play_one_round()