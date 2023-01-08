from test_data import test_data


def transaction_validator(func):
    def wrapper(*args, **kwargs):
        # 1. `trans_sum` must > 0
        if args[2] < 0:
            print(f"error: sum cannot be less than 0")
            return False
        # 2. `from_object.balance` must be >= `trans_sum`
        if args[0]['balance'] <= args[2]:
            print(f"error: `from_object.balance` must be >= `trans_sum`")
            return False
        # 3. both objects `is_active` is True
        if args[0]['is_active'] is False or args[1]['is_active'] is False:
            print(f"error: both objects is not active")
            return False
        # if any not ok print error and stop operation
        res = func(*args, **kwargs)
        return res

    return wrapper


@transaction_validator
def transaction(from_object, to_object, trans_sum):
    balance_01 = from_object['balance']
    balance_02 = to_object['balance']
    sum_01 = balance_01 - trans_sum
    sum_02 = balance_02 + trans_sum
    return sum_01, sum_02


def test_transactions():
    for el in test_data:
        trans_sum_ = el['trans_sum']
        from_object_ = el['from_object']
        to_object_ = el['to_object']
        res = transaction(from_object_, to_object_, trans_sum_)
        if res:
            print(f'sum1: {res[0]}, sum2: {res[1]}')


test_transactions()


