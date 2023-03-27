from function import display
input_price = input("Enter your motorcycle price : ")
try:
    input_price = int(input_number)
except ValueError:
    try:
        input_price = float(input_number)
    except ValueError:
        print("Invalid input. Please enter an integer or a float price.")
        exit()
result = display(input_price)
print(result)
