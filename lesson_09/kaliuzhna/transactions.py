from test_data import test_data


def transaction_validator(func):
    def wrapper(from_object, to_object, trans_sum, *args, **kwargs):
        print(f"we are going to make a transaction from {from_object} to {to_object} with trans_sum {trans_sum}")
        if trans_sum <= 0:
            print(f"trans_sum {trans_sum} must be > 0")
            return False
        if from_object["balance"] < trans_sum:
            print("error: not enough money in the account")
            return False
        if from_object["is_active"] is False or to_object["is_active"] is False:
            print("error: one or both objects have False `is_active` ")
            return False
        return func(from_object, to_object, trans_sum, *args, **kwargs)

    return wrapper


@transaction_validator
def transaction(from_object, to_object, trans_sum):
    from_object["balance"] -= trans_sum
    to_object["balance"] += trans_sum
    return from_object["balance"], to_object["balance"], trans_sum


def test_transactions():
    for trans in test_data:
        from_object = trans["from_object"]
        to_object = trans["to_object"]
        trans_sum = trans["trans_sum"]
        print(transaction(from_object, to_object, trans_sum))


test_transactions()