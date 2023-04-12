from function import calculate_monthly_payment, validate_price
import pytest

#calculate_monthly
@pytest.mark.code
def test_price_input_150000():
    input1 = 150000
    input2 = 75000
    expected_result = 500
    actual_result = calculate_monthly_payment(input1, input2)
    assert expected_result == actual_result

@pytest.mark.code
def test_price_input_150000_50():
    input1 = 150000.50
    input2 = 75000.25
    expected_result = 500.00
    actual_result = calculate_monthly_payment(input1, input2)
    assert expected_result == actual_result

#validate
@pytest.mark.validate
def test_price_int_input_150000():
    input1 = 150000
    input2 = 75000
    expected_result = (150000,75000)
    actual_result = validate_price(input1, input2)
    assert expected_result == actual_result

@pytest.mark.validate
def test_price_int_input_150000_50():
    input = 150000.50
    expected_result = 150000.50
    actual_result = validate_price(input)
    assert expected_result == actual_result    

@pytest.mark.validate
def test_price_zero_input():
    input1 = 0
    input2 = 0
    expected_result = "Error: Please input positive integer or float price"
    actual_result = validate_price(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_price_negative_input():
    input1 = -1
    input2 = -1
    expected_result = "Error: Price must be a positive non-zero number"
    actual_result = validate_price(input1, input2)
    assert expected_result == actual_result

@pytest.mark.validate
def test_price_negative_float():
    input = -1.5
    expected_result = "Error: Price must be a positive non-zero number"
    actual_result = validate_price(input)
    assert expected_result == actual_result
   
@pytest.mark.validate
def test_price_str_input_1():
    input = "a"
    expected_result = "Error: Please input positive integer or float price"
    actual_result = validate_price(input)
    assert expected_result == actual_result
   
@pytest.mark.validate
def test_price_str_input_2():
    input = "&"
    expected_result = "Error: Please input positive integer or float price"
    actual_result = validate_price(input)
    assert expected_result == actual_result
