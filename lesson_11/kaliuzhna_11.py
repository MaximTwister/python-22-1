from operator import add
from operator import mul
from operator import mod
from operator import pow
from operator import truediv

def gen_init(func):
    def wrapper(*args, **kwargs):
        g = func(*args, **kwargs)
        next(g)
        return g
    return wrapper


@gen_init
def multiplier():
    history = []
    while True:
        data = yield
        value_one = data.get('value_one')
        value_two = data.get('value_two')
        action = data.get('action')
        cmd = data.get('cmd')

        if cmd == "history":
            print(history)
            continue

        if action == "*":
            res = mul(value_one, value_two)
        elif action == "+":
            res = add(value_one, value_two)
        elif action == "%":
            res = mod(value_one, value_two)
        elif action == "**":
            res = pow(value_one, value_two)
        elif action == "/":
            if value_two != 0:
                res = truediv(value_one, value_two)
            else:
                res = "can't divide by zero"
        else:
            res = "calculator does not yet support this operation"

        history.append({
            f"{value_one} {action} {value_two} = {res}"
        })
        yield res


gen = multiplier()