from test_data import test_data


TRANS_SUM_ERROR = "[ERROR] transaction sum must be positive number"
OBJECT_BALANCE_ERROR = "[ERROR] object balance must be equal or more than transaction sum"
OBJECT_STATUS_ERROR = "[ERROR] both objects must be active to perform transaction."


def transaction_validator(do_transaction_function):
    def wrapper(*args, **kwargs) -> (str | None, dict):

        err = None
        data = kwargs.get("data")
        from_object = data.get("from_object")
        to_object = data.get("to_object")
        trans_sum = data.get("trans_sum")

        # 1. `trans_sum` must > 0
        if not trans_sum > 0:
            err = TRANS_SUM_ERROR

        # 2. `from_object.balance` must be >= `trans_sum`
        elif not from_object.get("balance") >= trans_sum:
            err = OBJECT_BALANCE_ERROR

        # 3. both objects `is_active` is True
        elif not all([from_object.get("is_active"), to_object.get("is_active")]):
            err = OBJECT_STATUS_ERROR

        if not err:
            do_transaction_function(from_object, to_object, trans_sum)

        return err, data

    return wrapper


@transaction_validator
def do_transaction(from_object, to_object, trans_sum):
    from_object["balance"] -= trans_sum
    to_object["balance"] += trans_sum


def test_transactions():

    want_errors = {
        TRANS_SUM_ERROR: 3,
        OBJECT_BALANCE_ERROR: 6,
        OBJECT_STATUS_ERROR: 6,
    }

    got_errors = {
        TRANS_SUM_ERROR: 0,
        OBJECT_BALANCE_ERROR: 0,
        OBJECT_STATUS_ERROR: 0,
    }

    want_valid_data = []
    got_valid_data = []

    for test in test_data:
        err, data = do_transaction(data=test)

        if err:
            got_errors[err] += 1
        else:
            got_valid_data.append(data)

    try:
        assert want_errors != got_errors
    except AssertionError as e:
        print(f"wants errors: {want_errors}\ngot errors: {got_errors}")


test_transactions()
