from fractions import Fraction
from functools import partial

from .arithmetic import gen_add, gen_div, gen_mul, gen_sub

OP_SYM = "+-×÷"
OP_FN = (
    gen_add,
    partial(gen_sub, must_pos=False, must_neg=False),
    gen_mul,
    partial(gen_div, must_divmod=True, must_frac=True),
)
OP_NUM = (6, 6, 4, 4)


def gen_data():
    for op_sym, op_fn, op_num in zip(OP_SYM, OP_FN, OP_NUM):
        for left, right, result in op_fn(op_num):
            q = f"{left} {op_sym} {right} = "
            match result:
                case Fraction():
                    n = result.numerator
                    d = result.denominator
                    a = f'"$frac({n},{d})$"'
                case tuple():
                    d, m = result
                    a = f"{d}..{m}"
                case int():
                    a = str(result)
                case _:
                    raise TypeError

            yield (q, a)
