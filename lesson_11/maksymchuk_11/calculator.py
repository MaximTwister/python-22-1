from common import math_operations_mapper
from utils import get_key_by_value


def generator_init(func_generator):
    def wrapper(*args, **kwargs):
        activated_generator = func_generator(*args, **kwargs)
        next(activated_generator)
        return activated_generator
    return wrapper


@generator_init
def calculator():
    history = []
    while True:
        res = None
        data = yield
        a, b, op, cmd = data

        if cmd == "c":
            res = op(a, b)
            math_op_human_friendly = get_key_by_value(_dict=math_operations_mapper, _value=op)
            history.append(
                {"operation": math_op_human_friendly, "a": a, "b": b, "res": res})
        elif cmd == "h":
            res = history

        yield res


calc = calculator()
