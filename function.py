def validate_number(price):
    if type(price) == str:
        return "Error: Please input integer or float price"
    elif price <= 0:
        return "Error: Price must be a positive non-zero number"
    else:
        return price
    
def number_to_month(number):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    return months[number - 1]

def display_month(number):
    result = validate_number(number)
    if type(result) == int:
        return number_to_month(result)
    return result
