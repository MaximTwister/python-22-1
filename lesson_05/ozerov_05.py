import sys

currencies_map = {
    "USD_UAH": 40.7,
    "UAH_USD": 0.027,
}


def currency_converter(currency_from, currency_to, currency_from_val):
    if currency_from_val > 0:
        currencies_pair = currency_from + "_" + currency_to
        currencies_ratio = currencies_map.get(currencies_pair, 0.0)
        return currency_from_val * currencies_ratio
    else:
        print("Value must be greater than 0")
        sys.exit()


def update_currencies_map(currency_from, currency_to, currency_from_val):
    update_currencies_pair = currency_from + "_" + currency_to
    currencies_map[update_currencies_pair] = currency_from_val
    return update_currencies_pair


currency_to_val = currency_converter("USD", "UAH", 1000)
print(f"Calculation done with result: {currency_to_val}")
update_currency_to_val = update_currencies_map("EUR", "UAH", 40)
print(currencies_map)
