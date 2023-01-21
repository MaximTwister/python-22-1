from operator import add, sub, truediv, mul

operators = ("+", "-", "/", "*")

def calculator():
    history = []
    while True:
        values = yield
        if values is None:
            break
        value_1, value_2, math_operator = values
        res = math_operator(value_1, value_2)
        history.append({
            "value_1": value_1,
            "value_2": value_2,
            "res": res,
            "operation": math_operator.__name__
        })
        print(history)
        yield res


c = calculator()


def input_to_calculator():
    while True:
        try:
            value_1 = int(input("Enter first value: "))
            value_2 = int(input("Enter second value: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        try:
            m_operator = str(input("Enter math operator: "))
            if m_operator in operators:
                next(c)
                if m_operator == "+":
                    print(c.send((value_1, value_2, add)))
                elif m_operator == "-":
                    print(c.send((value_1, value_2, sub)))
                elif m_operator == "/":
                    if value_2 != 0:
                        print(c.send((value_1, value_2, truediv)))
                    else:
                        print("Can't divide by zero!")
                elif m_operator == "*":
                    print(c.send((value_1, value_2, mul)))
                next_calculation = input('Lets do next calculation?(yes/no): ')
                if next_calculation == 'no':
                    break
                elif next_calculation == 'yes':
                    pass
                else:
                    print('I dont understand you')
        except ValueError:
            print("Is not operation")


input_to_calculator()