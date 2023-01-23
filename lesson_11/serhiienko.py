import operator


сalculator_operator = {
  "+": operator.add,
  "*": operator.mul,
  "%": operator.mod,
  "**": operator.pow,
  "/": operator.truediv
}  


def auto_init(func):
  def wrapper(*args, **kwargs):
    g = func(*args, **kwargs) 
    next(g)
    return g
  return wrapper


@auto_init
def сalculator():
  history = []
  id = 1
  
  while True:
    options = yield 

    value_first = options.get("value_first")
    value_second = options.get("value_second")
    action = options.get("action")
    cmd = options.get("cmd")

    if cmd == "history":
      print(history)
      continue

    if type(value_first) not in [int, float] or type(value_second) not in [int, float]:
      print("Pass two numbers!")
      continue

    if not value_first or not value_second:
      print("Pass two values!")
      continue

    if action not in сalculator_operator:
      print("This operator is not supported!")
      continue

    try:
      result = сalculator_operator[action](value_first, value_second)
      history.append({ id: f"{value_first} {action} {value_second} = {result}" })
      id += 1
      print("result", result)
      yield result
    except ZeroDivisionError:
      print("Can't divide by zero!") 
    

gen_сalc = сalculator()
