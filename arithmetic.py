from fractions import Fraction
from random import randint
from typing import Generator

type T_Generator_int = Generator[tuple[int, int, int], None, None]


def gen_add(num: int = 5) -> T_Generator_int:
    """生成二、三位数混合加法计算"""
    for _ in range(num):
        left = randint(10, 1000)
        right = randint(10, 1000)
        result = left + right
        yield (left, right, result)


def gen_sub(
    num: int = 5, must_pos: bool = True, must_neg: bool = False
) -> T_Generator_int:
    """生成二、三位数混合减法计算"""
    for _ in range(num):
        while True:
            left = randint(10, 1000)
            right = randint(10, 1000)
            if left != right:
                break
        if (must_pos and left < right) or (must_neg and left > right):
            left, right = right, left

        result = left - right
        yield (left, right, result)


def gen_mul(num: int = 5) -> T_Generator_int:
    """生成二、三位数混合乘法计算"""
    for _ in range(num):
        left = randint(10, 100)
        right = randint(10, 100)
        result = left * right
        yield (left, right, result)


def gen_div(
    num: int = 5, must_divmod: bool = True, must_frac: bool = True
) -> Generator[
    tuple[int, int, int | Fraction | tuple[int, int]],
    None,
    None,
]:
    """除法较为复杂。
    最简单的是整除，其次是余数除法，接着是小数和分数。

    分为两类：
    - 可以整除
    - 不能整除，表示为余数和分数
    """
    if must_divmod:

        def f():
            while True:
                n1 = randint(10, 201)
                n2 = randint(2, 10) * randint(2, 10)
                if n1 % n2 != 0:
                    break
            return (n1, n2, divmod(n1, n2))

        for _ in range(num):
            yield f()

    elif must_frac:

        def f_finite():
            n1 = randint(2, 201)
            n2 = randint(2, 10) * randint(2, 10)
            return (n1, n2, Fraction(n1, n2))

        yield from (f_finite() for _ in range(num))

    else:
        # 根据答案出题
        def f_int():
            n1 = randint(10, 51)
            n2 = randint(2, 10)
            return (n1 * n2, n2, n1)

        yield from (f_int() for _ in range(num))
