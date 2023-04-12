from function import display_monthly_payment

input_price = input("Enter your motorcycle price : ")
input_down_price = input("Enter your motorcycle down price : ")

try:
    input_price = int(input_price)
except ValueError:
    try:
        input_price = float(input_price)
    except ValueError:
        exit()

try:
    input_down_price = int(input_down_price)
except ValueError:
    try:
        input_down_price = float(input_down_price)
    except ValueError:
        exit()

result = display_monthly_payment(input_price, input_down_price)
print(result)
