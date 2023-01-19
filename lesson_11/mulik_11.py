from operator import mul, truediv


def calculator():
    history = []
    while True:
        values = yield
        if not values:
            break
        a, b, op = values
        res = op(a, b)
        history.append({
         "a": a, "b": b, "res": res, "operation": op
        })
        yield res
    return history


calc = calculator()


def tttt():
    while True:
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        op = input("Enter operation: ")
        calc.__next__()
        if op == "*":
            print(calc.send((a, b, mul)))
        elif op == "/":
            print(calc.send((a, b, truediv)))
        else:
            print("Such an operation in development")
            print(calc.send(None))


tttt()