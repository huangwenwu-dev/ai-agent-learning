def is_even(n: int) -> bool:
    """判断一个整数是否为偶数.

    Args:
    n (int): 要判断的整数

    Returns:
        bool: 偶数返回 True, 奇数返回 False
    """
    return n % 2 == 0

print(is_even(4))
print(is_even(7))