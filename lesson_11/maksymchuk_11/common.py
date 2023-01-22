from operator import mul, sub, add, truediv


math_operations_mapper = {
    "-": sub,
    "+": add,
    "*": mul,
    "/": truediv,
}

commands_descr = {
    "h": "to see the history of all performed calculations",
    "c": "to perform the regular calculation",
}

empty_calculation_data = {"a": None, "b": None, "op": None}
