from function import calculate_monthly,validate_price
import pytest
#pytest -m code
#calculate
@pytest.mark.code
def test_price_input_150000():
    input = 150000
    expected_result = 500
    actual_result = calculate_monthly(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_price_input_150000_50():
    input = 150000.50
    expected_result = 500.001666667
    actual_result = calculate_monthly(input)
    assert expected_result == actual_result

#validate
@pytest.mark.validate
def test_price_int_input_150000():
    input = 150000
    expected_result = 150000
    actual_result = validate_price(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_price_int_input_150000_50():
    input = 150000.50
    expected_result = 150000.50
    actual_result = validate_price(input)
    assert expected_result == actual_result    

@pytest.mark.validate
def test_price_zero_input():
    input = 0
    expected_result = "Error: Price must be a positive non-zero number"
    actual_result = validate_price(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_price_negative_input():
    input = -1
    expected_result = "Error: Price must be a positive non-zero number"
    actual_result = validate_price(input)
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
    expected_result = "Error: Please input integer or float price"
    actual_result = validate_price(input)
    assert expected_result == actual_result
   
@pytest.mark.validate
def test_price_str_input_2():
    input = "&"
    expected_result = "Error: Please input integer or float price"
    actual_result = validate_price(input)
    assert expected_result == actual_result
