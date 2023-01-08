from test_data import test_data


def transaction_validator(func):
  def wrapper(*args, **kwargs):
    from_object = args[0]
    to_object = args[1]
    trans_sum = args[2]

    # 1. `trans_sum` must > 0
    if trans_sum < 0:
        print(f"error: transaction amount must be greater than 0")
        return False

    # 2. `from_object.balance` must be >= `trans_sum`
    if from_object.get("balance") <= trans_sum:
        print(f"error: balance must be >= transaction amount")
        return False

    # 3. both objects `is_active` is True
    if from_object.get("is_active") is False or to_object.get("is_active") is False:
        print(f"error: both objects isn`t active")
        return False

    # if any not ok print error and stop operation
    return func(*args, **kwargs)
  return wrapper


@transaction_validator
def transaction(from_object, to_object, trans_sum):
  from_balance = from_object.get("balance")
  to_balance = to_object.get("balance")
  from_object["balance"] = from_balance - trans_sum
  to_object["balance"] = to_balance + trans_sum
  return from_object, to_object


def test_transactions():
  for data in test_data:
    trans_sum = data.get('trans_sum')
    from_object = data.get('from_object')
    to_object = data.get('to_object')
    res = transaction(from_object, to_object, trans_sum)
    
    if res:
        print(f'sum1: {res[0]}, sum2: {res[1]}')


test_transactions()