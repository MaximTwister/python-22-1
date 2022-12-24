# 1. To inform users, that such value isn`t available
# 2. To be sure, that value is positive and to inform users, that value is incorrect
# 3. To exchange 1000$ in UAH
# 4. Make new function, which will add new exchange pairs

currencies_map = {"USD_UAH": 40.7, "EUR_UAH": 37}


def currency_converter(currency_from, currency_to, currency_from_val):
    if currency_from_val < 0:
        print ("value is incorrect, please, write down positive one")
    exchange_pair = currency_from + "_" + currency_to
    if exchange_pair not in currencies_map.keys():
        print("This currency is not available now. Please choose other one")
    exchange = currencies_map.get(exchange_pair, 0.0)
    return exchange * currency_from_val

new_val = currency_converter("USD", "UAH", 1000)
print(f"Calculation is completed: {new_val}")

def update_currencies_map(currency_from, currency_to, currencies_from_val):
    New_pairs = dict(zip([currency_from + "_" + currency_to], [currencies_from_val]))
    currencies_map.update(New_pairs)

new_pair1 = update_currencies_map("USD", "UAH", 37.7)
new_pair2= update_currencies_map("EUR", "UAH", 38.73)
new_pair3 = update_currencies_map("PLN", "UAH", 8.27)

print(currencies_map)