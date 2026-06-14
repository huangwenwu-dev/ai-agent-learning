import random

def play_one_round():
    """
    执行一局猜数游戏。
    返回:
        True  : 玩家猜中了
        False : 玩家用尽7次机会仍未猜中
    """
    secret = random.randint(1, 100)    # 随机生成1~100直接的秘密数字
    attempts = 0                        # 当前已尝试次数
    max_attempts = 7                    # 最大允许次数

    print("\n===== 新的一局! 猜1~100之间的数字 =====")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        guess_str = input(f"还剩{remaining} 次机会, 请输入数字: ")

        # 容错处理: 非数字输入不消化次数
        try:
            guess = int(guess_str)
        except ValueError:
            print("❌ 无效输入, 请输入一个整数! ")
            continue

        attempts += 1

        if guess < secret:
            print("太小了")
        elif guess > secret:
            print("太大了")
        else:
            print(f"恭喜猜中! 正确答案是{secret}, 用了 {attempts}次机会。 ")
            return True
        
        # 循环结束仍未猜中
        print(f"很遗憾，{max_attempts}次机会用完了。正确答案是{secret}。")
        return False

def main():
    """主循环: 支持多局游戏"""
    while True:
        win = play_one_round()
        again=input("再来一局吗？(y/n): ")
        if again.lower() != 'y':
            print("感谢游玩, 再见! ")
            break

if __name__ == "__main__":
    main()