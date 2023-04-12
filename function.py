def validate_price(price):
    if not isinstance(price, (int, float)):
        return "Error: Price must be a number"
    elif price <= 0:
        return "Error: Price must be a positive non-zero number"
    else:
        return None

def validate_down_payment(down_payment, price):
    if not isinstance(down_payment, (int, float)):
        return "Error: Down payment must be a number"
    elif down_payment <= 0:
        return "Error: Down payment must be a positive non-zero number"
    elif down_payment != 0.2 * price:
        return "Error: Down payment must be 20 percent of the price"
    else:
        return None

def validate_price_and_down_payment(price, down_payment):
    price_error = validate_price(price)
    down_error = validate_down_payment(down_payment, price)
    if price_error and down_error:
        return price_error + " and " + down_error
    if price_error:
        return price_error
    if down_error:
        return down_error 
    else:
        return (price, down_payment)

# def validate_price_and_down_payment(price, down_payment):
#     if not isinstance(down_payment, (int, float)) and isinstance(price, (int, float)):
#         return "Error: Price and Down Payment be number"
#     elif isinstance(price, str) and down_payment <= 0:
#         return "Error: Price Payment must not be string and Down Payment must be a positive non-zero number"
#     elif isinstance(down_payment, str) and price <= 0:
#         return "Error: Down Payment must not be string and Price must be a positive non-zero number"
#     elif isinstance(price, str):
#         return "Error: Price Payment must not be string" 
#     elif isinstance(down_payment, str):
#         return "Error: Down Payment must not be string"
#     elif price <= 0 and down_payment <= 0:
#         return "Error: Price and down_payment must be a positive non-zero number"
#     elif price <= 0 and down_payment > price:
#         return "Error: Price must be a positive non-zero number and Down payment cannot be greater than the price"
#     elif price < 0:
#         return "Error: Price must be a positive non-zero number"
#     elif down_payment <= 0:
#         return "Error: Down Payment must be a positive non-zero number"
#     elif down_payment != 0.2 * price:
#         return "Error: Down payment must be 20 percent of the price"
#     else:
#         return price, down_payment

def calculate_monthly_payment(price, down):
    monthly = ((price - down) * 0.05 ) / 12
    if type(monthly) == float:
        monthly_r = round(monthly, 2)
        return monthly_r
    return monthly

def display_monthly_payment(price, down):
    result = validate_price_and_down_payment(price,down)
    if type(result) == int or type(result) == float:
        return calculate_monthly_payment(result)
    return result