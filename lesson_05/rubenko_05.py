import sys

currencies_map = {
    "USD_UAH": 40.7,
    "UAH_USD": 0.027,
}


def update_currencies_map(currency_from, currency_to, currency_from_val):
    update_currencies_pair = currency_from + "_" + currency_to
    currencies_map[update_currencies_pair] = currency_from_val


def add_new_pair_currencies_map(currency_from, currency_to, currencies_ratio):
    if type(currencies_ratio) == int or type(currencies_ratio) == float:
        if currencies_ratio > 0:
            new_currencies_pair = currency_from + "_" + currency_to
            new_currencies_pair_with_ratio = {new_currencies_pair: currencies_ratio}
            return currencies_map.update(new_currencies_pair_with_ratio)
        else:
            print("currencies_ratio can't be equal to 0 or negative!")
            sys.exit()


def currency_converter(currency_from, currency_to, currency_from_val):
    if type(currency_from_val) == int or type(currency_from_val) == float:
        if currency_from_val >= 0:
            currencies_pair = currency_from + "_" + currency_to
            currencies_ratio = currencies_map.get(currencies_pair, 0.0)
            if currencies_ratio == 0 or currencies_ratio == 0.0:
                print("currency pair is not on our list or currencies_ratio <= 0! To add a new currency pair,"
                      " please use the \"def add_new_pair_currencies_map\". And check the value currencies_ratio ")
                sys.exit()
            else:
                return currency_from_val * currencies_ratio
        else:
            print(f"currency_from_val of must be a positive int or positive float!")
            sys.exit()
    else:
        print("currency_from_val is negative! Must be positive!")


print(f"Initial currencies_map = {currencies_map}")

add_new_pair_currencies_map("CAD", "CHF", 1.449)

print(f"After update currencies_map = {currencies_map}")

currency_to_val = currency_converter("USD", "UAH", 200.0)

print(f"Calculation done with result: {currency_to_val:.2f}")

currency_to_val = currency_converter("CAD", "CHF", 1000.0)

print(f"Calculation done with result: {currency_to_val:.2f}")

