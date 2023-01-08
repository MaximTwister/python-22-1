currencies_map = {
    "USD_UAH": 40.7,
    "UAH_USD": 0.027,
}


def currency_converter(currency_from, currency_to, currency_from_val):

    if type(currency_from_val) not in[int, float]:
        print("it's not number")
    if currency_from_val < 0:
        print("not positive integer")
    currencies_pair = currency_from + "_" + currency_to
    if currencies_pair not in currencies_map.keys():
        print("Currencies not aviable now")
    
    currencies_ratio = currencies_map.get(currencies_pair, 0.0)
    return currency_from_val * currencies_ratio

def update_currencies_map(currency_from, currency_to, currency_from_val):
    currency_pair = currency_from + "_" + currency_to
    currencies_map[currency_pair] = currency_from_val
    print(f"Currencies updated: {currencies_map}")

currency_to_val = currency_converter("USD", "UAH", 100)
print(f"Calculation done with result: {currency_to_val}")

update_currencies_map("EUR", "UAH", 42)


    
# 1. Inform user that such currencies pair is not supported yet.
# 2. Be sure that `currency_from_val` positive integer or float
#    2.1 Inform user that such value is incorrect
# 3. New function which adds new pairs with ratio to `currencies_map`:
#    function name: update_currencies_map
#    with params: currency_from, currency_to, currency_from_val
#    Inform user about results