from function import display_month
input_number = input("Enter number : ")
try:
    try:
        input_number = int(input_number)
    except:
        input_number = float(input_number)
except:
    input_number = str(input_number)
result = display_month(input_number)
print(result)
