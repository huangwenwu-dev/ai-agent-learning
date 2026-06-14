def is_even(n: int) -> bool:
    """判断偶数。 """
    return n % 2 == 0

def add(a: int, b: int) ->int:
    return a + b

def greet(name: str) -> None:
    print(f"你好, {name}! ")

def power(base: int, exp: int = 2) -> int:
    return base ** exp

if __name__ == "__main__":
    print("=== 测试 is_even ===")
    print(is_even(4))
    print(is_even(7))

    print("=== 测试 abb ===")
    print(add(3, 5))

    print("=== 测试 greet ===")
    greet("小明")

    print("=== 测试 power ===")
    print(power(4))
    print(power(2, 5))