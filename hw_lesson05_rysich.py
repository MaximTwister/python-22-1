currencies_map = {
    "USD_UAH": 40.7,
    "UAH_USD": 0.027,
}


def currency_converter(currency_from, currency_to, currency_from_val):
    currencies_pair = currency_from + "_" + currency_to
    currencies_ratio = currencies_map.get(currencies_pair, 0.0)
    if currencies_ratio == 0:
        print("Sorry, these currencies pair is not supported yet")
    else: return currency_from_val * currencies_ratio
# --------------------------------------------------------------------
def update_currencies_map(currency_from, currency_to, currency_from_val):
    currencies_pair = currency_from + "_" + currency_to
    new_currency = {currencies_pair: currency_from_val}
    currencies_map.update(new_currency)
    print(f"{new_currency}")
# --------------------------------------------------------------------
print(f"Hello! This is my currency converter!")

value = 0
curr_from = input("Please input currency from: ") 
curr_to = input("Please input currency to: ")

while(value <= 0):
    value = float(input("Input value (only positive): "))
    if value < 0:
        print("Sorry, you just input negative value. Try again")
    else:
        print(f"1. Convert \n2. Update")
        choose = int(input())
        if choose == 1:
            currency_to_val = currency_converter(curr_from, curr_to, value)
            print(f"Calculation done with result: {currency_to_val}")
        elif choose == 2:
            update_currencies_map(curr_from, curr_to, value)
        else: print("incorrect input")
