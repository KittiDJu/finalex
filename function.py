def validate_price(price):
    if isinstance(price, str) or price == 0:
        return "Error: Please input positive integer or float price"
    elif price < 0:
        return "Error: Price must be a positive non-zero number"
    else:
        return price

def calculate_down_payment(price):
    down = 20 / 100 * (price)
    if type(down) == float:
        down_r = round(down, 2)
        return down_r
    return down

def calculate_monthly_payment(price):
    down = calculate_down_payment(price)
    monthly = ((price - down) * 5 / 100 ) / 12
    if type(monthly) == float:
        monthly_r = round(monthly, 2)
        return monthly_r
    return monthly

def display_down_payment(price):
    result = validate_price(price)
    if type(result) == int or type(result) == float:
        return calculate_down_payment(result)
    return result

def display_monthly_payment(price):
    result = validate_price(price)
    if type(result) == int or type(result) == float:
        return calculate_monthly_payment(result)
    return result