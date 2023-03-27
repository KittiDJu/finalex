def validate_price(price):
    if isinstance(price, str) or price == 0:
        return "Error: Please input positive integer or float price"
    elif price < 0:
        return "Error: Price must be a positive non-zero number"
    else:
        return price

def calculate_monthly(price):
    down = 20/100 * (price)
    monthly = ((price - down) * 5 / 100 ) / 12
    return monthly

def display_monthly(price):
    result = validate_price(price)
    if type(result) == int && type(result) == float:
        return calculate_monthly(result)
    return result
