from logger import logger


currencies_map = {
    "USD_UAH": 40.7,
    "UAH_USD": 0.027,
}


def currency_converter(currency_from, currency_to, currency_from_val):
    currencies_pair = currency_from + "_" + currency_to

    if currencies_pair not in currencies_map:
        logger("Such currencies pair is not supported yet.", "info")
        return None

    if type(currency_from_val) not in [int, float]:
        logger("The argument you passed is not a number.", "error")
        return None

    if currency_from_val < 0:
        logger("Current currency amount cannot be negative.", "error")
        return None

    currencies_ratio = currencies_map.get(currencies_pair)

    return currency_from_val * currencies_ratio


def update_currencies_map(currency_from, currency_to, currency_from_val):
    currencies_pair = currency_from + "_" + currency_to

    if type(currency_from_val) not in [int, float]:
        logger("The argument you passed is not a number.", "error")
        return

    if currency_from_val < 0:
        logger("Current currency amount cannot be negative.", "error")
        return

    if currencies_pair in currencies_map:
        currencies_map.update([(currencies_pair, currency_from_val)])
        logger("Update old currency pair.", "success")
    else:
        currencies_map[currencies_pair] = currency_from_val
        logger("Added new currency pair.", "success")


update_currencies_map("USD", "UAH", 50)
update_currencies_map("EUR", "UAH", 41.450)

calc = currency_converter("USD", "UAH", 1000)

print(f"Result: {calc}")
