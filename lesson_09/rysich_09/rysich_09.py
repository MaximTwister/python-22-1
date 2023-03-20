from test_data import test_data

SUM_POS_ERR = "[ERROR] transaction sum must be positive number"
BAL_EQ_ERR = "[ERROR] object balance must be equal or more than transaction sum"
STATUS_ERR = "[ERROR] both objects must be active to perform transaction."

def transaction_validator(transaction):
    def wrapper(data):
        err = None
        trans_sum = data.get("trans_sum")
        from_object = data.get("from_object")
        to_object = data.get("to_object")

        # 1. `trans_sum` must > 0
        if not trans_sum > 0:
            err = SUM_POS_ERR

        # 2. `from_object.balance` must be >= `trans_sum`
        elif not from_object.get("balance") >= trans_sum:
            err = BAL_EQ_ERR

        # 3. both objects `is_active` is True
        elif not all([from_object.get("is_active"), to_object.get("is_active")]):
            err = STATUS_ERR
        # if any not ok print error and stop operation
        if not err:
            transaction(from_object, to_object, trans_sum)
        return err
    return wrapper

@transaction_validator
def transaction(from_object, to_object, trans_sum):
    from_object["balance"] -= trans_sum
    to_object["balance"] += trans_sum

def test_transactions():
    catched_error = {
        SUM_POS_ERR: 0,
        BAL_EQ_ERR: 0,
        STATUS_ERR: 0
    }
    got_valid_data = []

    for test in test_data:
        if transaction(test):
            catched_error[transaction(test)] += 1
    print(f"\ngot errors: {catched_error}")

test_transactions()