currencies_map = {"USD_UAN": 40.7, "UAN_USD": 0.027}


def currency_converter(currency_from, currency_to, currency_from_val):
    if type(currency_from_val) not in [int, float]:
        print("it's not a number")
    if currency_from_val < 0:
        print("currency_from_val negative integer: ", currency_from_val)
    currencies_pair = currency_from + "_" + currency_to
    if currencies_pair not in currencies_map.keys():
        print("such currencies pair is not supported yet")
    currencies_ratio = currencies_map.get(currencies_pair, 0.0)
    return currency_from_val * currencies_ratio


currency_to_val = currency_converter("USD", "UAN", 1000)
print(f"Calculation done : {currency_to_val}")


def update_currencies_map (currency_from, currency_to, currency_from_val):
    update_currencies_pair = currency_from + "_" + currency_to
    currencies_map[update_currencies_pair] = currency_from_val


update_currency_to_val = update_currencies_map("EUR", "UAH", 42)
print(currencies_map)




