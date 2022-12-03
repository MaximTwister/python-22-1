# 1. Inform user that such currencies pair is not supported yet.
# 2. Be sure that `currency_from_val` positive integer or float
#    2.1 Inform user that such value is incorrect
# 3. New function which adds new pairs with ratio to `currencies_map`:
#    function name: update_currencies_map
#    with params: currency_from, currency_to, currency_from_val
#    Inform user about results



currencies_map = {
    "USD_UAH": 40.7,
    "UAH_USD": 0.027,
}


def currency_converter(currency_from, currency_to, currency_from_val):
    counter = 0
    if type(currency_from) == str:
        if currency_from.isalpha():
            if len(currency_from) == 3:
                if currency_from.upper() == currency_from:
                    counter += 1
                else:
                    print(f"Currency_from: {currency_from} is not upper")
            else:
                print(f"Length of currency_from: {currency_from} is not equal to 3 characters")
        else:
            print(f"Currency_from: {currency_from} is not alpha")
    else:
        print(f"Currency_from: {currency_from} isn`t string")
    if type(currency_to) == str:
        if currency_to.isalpha():
            if len(currency_to) == 3:
                if currency_to.upper() == currency_to:
                    if currency_from != currency_to:
                        counter += 1
                    else:
                        print(f"Values Currency_from: {currency_from} and Currency_to: {currency_to} are the same.")
                else:
                    print(f"Currency_to: {currency_to} is not upper")
            else:
                print(f"Length of currency_to: {currency_to} is not equal to 3 characters")
        else:
            print(f"Currency_to: {currency_to} is not alpha")
    else:
        print(f"Currency_to: {currency_to} isn`t string")

    if isinstance(currency_from_val, (float, int)) and currency_from_val > 0:
        counter += 1
    else:
        print(f"Currency_from_val: {currency_from_val} isn`t positive integer or float")
    if counter == 3:
        currencies_pair = currency_from + "_" + currency_to
        currencies_ratio = currencies_map.get(currencies_pair, 0.0)
        if currencies_ratio != 0.0:
            return currency_from_val * currencies_ratio

        print("Such currencies pair is not supported yet. Please, add these value with function Update_currencies_map")
        return


currency_to_val = currency_converter("USD", "USD", -100.1)
print(f"Calculation done with result: {currency_to_val}")



def update_currencies_map(currency_from, currency_to, currencies_ratio):
    new_dict = dict(zip([currency_from + "_" + currency_to], [currencies_ratio]))
    currencies_map.update(new_dict)
    return new_dict


new_map = update_currencies_map("USD", "UAH", 40.7)
new_map = update_currencies_map("EUR", "UAH", 41.450)
new_map = update_currencies_map("PLN", "UAH", 8.750)
new_map = update_currencies_map("GBP", "UAH", 47.225)
new_map = update_currencies_map("CHF", "UAH", 41.200)

print(currencies_map)