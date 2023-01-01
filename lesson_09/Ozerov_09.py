from test_data import test_data


def transaction_validator(func):
    def wrapper(*args, **kwargs):
        # 1. `trans_sum` must > 0
        if args[2] < 0:
            print(f"error: transaction amount must be greater than 0")
            return False
        # 2. `from_object.balance` must be >= `trans_sum`
        if args[0]['balance'] <= args[2]:
            print(f"error: balance must be >= transaction amount")
            return False
        # 3. both objects `is_active` is True
        if args[0]['is_active'] is False or args[1]['is_active'] is False:
            print(f"error: both objects isn`t active")
            return False
        # if any not ok print error and stop operation
        res = func(*args, **kwargs)
        return res
    return wrapper


@transaction_validator
def transaction(from_object, to_object, trans_sum):
    first_balance = from_object['balance']
    second_balance = to_object['balance']
    sum_01 = first_balance - trans_sum
    sum_02 = second_balance + trans_sum
    return sum_01, sum_02


def test_transactions():
    for e in test_data:
        e_trans_sum = e['trans_sum']
        e_from_object = e['from_object']
        e_to_object = e['to_object']
        res = transaction(e_from_object, e_to_object, e_trans_sum)
        if res:
            print(f'sum1: {res[0]}, sum2: {res[1]}')


test_transactions()
