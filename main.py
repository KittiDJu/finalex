from function import display
input_price = input("Enter your motorcycle price : ")
try:
    input_price = int(input_price)
except ValueError:
    try:
        input_price = float(input_price)
    except ValueError:
        print("Invalid input. Please enter an integer or a float price.")
        exit()
result = input_price(input_price)
print(result)
