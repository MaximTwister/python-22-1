currencies_map = {
    "USD_UAH": 40.7,
    "UAH_USD": 0.027,
}


def currency_converter(currency_from, currency_to, currency_from_val):
    currencies_pair = currency_from + "_" + currency_to
    currencies_ratio = currencies_map.get(currencies_pair, 0.0)
    return currency_from_val * currencies_ratio


currency_to_val = currency_converter("USD", "UAH", -100)
print(f"Calculation done with result: {currency_to_val}")

# 1. Inform user that such currencies pair is not supported yet.
# 2. Be sure that `currency_from_val` positive integer or float
#    2.1 Inform user that such value is incorrect
# 3. New function which adds new pairs with ratio to `currencies_map`:
#    function name: update_currencies_map
#    with params: currency_from, currency_to, currency_from_val
#    Inform user about results
