import random

def play_one_round():
    """一局猜数字游戏，返回 True 表示猜中，False 表示失败"""
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\n===== 新的一局！猜1~100之间的数字 =====")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        guess_str = input(f"还剩 {remaining} 次机会，请输入数字：")

        # 处理非数字输入
        try:
            guess = int(guess_str)
        except ValueError:
            print("❌ 无效输入，请输入一个整数！")
            continue   # 不增加 attempts

        attempts += 1

        if guess < secret:
            print("📉 太小了")
        elif guess > secret:
            print("📈 太大了")
        else:
            print(f"🎉 恭喜猜中！正确答案就是 {secret}，你用了 {attempts} 次机会。")
            return True

    # 超过最大次数仍未猜中
    print(f"😭 很遗憾，7次机会用完了。正确答案是 {secret}。")
    return False


def main():
    """主程序：反复进行游戏直到用户选择退出"""
    while True:
        win = play_one_round()          # 先玩一局
        again = input("\n再玩一局吗？(y/n)：")
        if again.lower() != 'y':
            print("感谢游玩，再见！👋")
            break


if __name__ == "__main__":
    main()