"""一个简单的计算器模块"""


def add(a, b):
    """返回两个数的和"""
    return a + b


def subtract(a, b):
    """返回两个数的差"""
    return a - b


def multiply(a, b):
    """返回两个数的积"""
    return a * b


def divide(a, b):
    """返回两个数的商，除数为 0 时抛出 ValueError"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


def power(a, b):
    """返回 a 的 b 次方"""
    return a ** b
def modulo(a, b):
    """返回 a 除以 b 的余数，除数为 0 时抛出 ValueError"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a % b


def average(a, b):
    """返回两个数的平均值"""
    return (a + b) // 2


if __name__ == "__main__":
    print("3 + 5 =", add(3, 5))
    print("10 - 4 =", subtract(10, 4))
    print("3 * 5 =", multiply(3, 5))
    print("10 / 4 =", divide(10, 4))
    print("2 ^ 10 =", power(2, 10))
    print("10 % 3 =", modulo(10, 3))
    print("4 和 6 的平均值 =", average(4, 6))
    try:
        divide(1, 0)
    except ValueError as e:
        print("除零测试:", e)
