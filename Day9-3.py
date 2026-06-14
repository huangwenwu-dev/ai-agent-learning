def add(a: int, b: int) -> int:
    """返回两个整数的和. """
    return a + b

def greet(name: str) -> None:
    """打印问候语. """
    print(f"你好, {name}! ")

def power(base: int, exp: int = 2) -> int:
    """返回 base 的 exp 次幂, 默认 exp=2. """
    return base ** exp

result = add(3, 5)
print(f"add(3, 5) = {result}")

greet("小明")

print(f"power(3) = {power(3)}")
print(f"power(2, 4) = {power(2, 4)}")