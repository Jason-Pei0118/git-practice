"""一个简单的计算器模块"""


def add(a, b):
    """返回两个数的和"""
    return a + b


def subtract(a, b):
    """返回两个数的差"""
    return a - b


if __name__ == "__main__":
    print("3 + 5 =", add(3, 5))
    print("10 - 4 =", subtract(10, 4))
