from test_data import test_data


def transaction_validator(func):
    def wrapper(*args, **kwargs):
        # 1. `trans_sum` must > 0
        if args[2] < 0:
            print(f'error: sum transaction = {args[2]} it mast be > 0 ')
            return False
        # 2. `from_object.balance` must be >= `trans_sum`
        if args[0]['balance'] <= args[2]:
            balance = args[0]['balance']
            print(f'error: from_object_balance = {balance}, but must be >= trans_sum {args[2]}')
            return False
        # 3. both objects `is_active` is True
        if args[0]['is_active'] or args[1]['is_active'] is False:
            print('error: both objects is not active')
        # if any not ok print error and stop operation
        res = func(*args, **kwargs)
        return res

    return wrapper


@transaction_validator
def transaction(from_object, to_object, trans_sum):
    # Write transaction logic
    from_object_balance = from_object['balance']
    to_object_balance = to_object['balance']
    from_object_sum = from_object_balance - trans_sum
    to_object_sum = to_object_balance + trans_sum
    return from_object_sum, to_object_sum


def test_transactions():
    for el in test_data:
        trans_sum = el['trans_sum']
        from_object = el['from_object']
        to_object = el['to_object']
        res = transaction(from_object, to_object, trans_sum)
        if res:
            print(f'from_object_sum: {res[0]}, to_object_sum: {res[1]}')


test_transactions()
