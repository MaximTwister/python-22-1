from test_data import test_data


def transaction_validator(func):
    def wrapper(*args, **kwargs):
        # 1. `trans_sum` must > 0
        # 2. `from_object.balance` must be >= `trans_sum`
        # 3. both objects `is_active` is True
        # if any not ok print error and stop operation
        func(*args, **kwargs)

    return wrapper


@transaction_validator
def transaction(from_object, to_object, trans_sum):
    # Write transaction logic
    pass


def test_transactions():
    pass
