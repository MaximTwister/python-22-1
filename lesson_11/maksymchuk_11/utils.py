from common import (
    empty_calculation_data,
    math_operations_mapper,
)


def get_calculation_data():
    data = empty_calculation_data
    err = None

    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    op = input(f"Enter math operation {list(math_operations_mapper)}: ")

    py_math_func = math_operations_mapper.get(op)
    if py_math_func is None:
        err = f"Math operation `{op}` is not supported."
    else:
        data["a"] = a
        data["b"] = b
        data["op"] = py_math_func

    return data, err


def stub():
    return empty_calculation_data, None


def get_key_by_value(_dict: dict, _value):
    return list(_dict)[list(_dict.values()).index(_value)]
