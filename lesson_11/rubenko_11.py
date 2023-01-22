from operator import mul, truediv, add, sub

math_op_symbol_tuple = ("*", "/", "+", "-")


def calculator():
    history = []
    while True:
        values = yield
        if values is None:
            break
        value_1, value_2, math_operator = values
        res = math_operator(value_1, value_2)
        history.append({
            "value_1": value_1, "value_2": value_2, "res": res, "operation": math_operator.__name__
        })
        print(history)
        yield res


calc = calculator()


def get_user_data():
    value_1 = 0
    value_2 = 0
    math_op = None
    while True:
        try:
            value_1 = int(input("Enter value_1 :"))
            if isinstance(value_1, int):
                pass
            else:
                break
        except ValueError as err:
            print(f"{err}")
            break
        try:
            value_2 = int(input("Enter value_2 :"))
            if isinstance(value_2, int):
                pass
            else:
                break
        except ValueError as err:
            print(f"{err}")
            break
        try:
            a = input(str("Enter math operator ( '*' or '/' or '+' or '-') :"))
            if a in math_op_symbol_tuple:
                math_op = a
            else:
                print(f"You entered not math symbol <{a}>!")
        except ValueError as err:
            print(f"{err}")
            break
        next(calc)
        if math_op == "*":
            print(calc.send((value_1, value_2, mul)))
        elif math_op == "/":
            print(calc.send((value_1, value_2, truediv)))
        if math_op == "+":
            print(calc.send((value_1, value_2, add)))
        elif math_op == "-":
            print(calc.send((value_1, value_2, sub)))


get_user_data()

