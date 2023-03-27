def validate_number(number):
    if type(number) != int:
        if type(number) == str:
            return "Error: Please input integer"
        elif number >= 1 and number <= 12:
            return "Error: Please input integer"
        else:
            return "Error: Month number out of range"
    elif number >= 1 and number <= 12:
        return number
    else:
        return "Error: Month number out of range"
    
def number_to_month(number):
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    return months[number - 1]

def display_month(number):
    result = validate_number(number)
    if type(result) == int:
        return number_to_month(result)
    return result
    


