from function import calculate_monthly_payment, validate_price_and_down_payment
import pytest

#calculate_monthly
@pytest.mark.code
def test_input_150000():
    input1 = 150000
    input2 = 30000
    expected_result = 500.00
    actual_result = calculate_monthly_payment(input1, input2)
    assert expected_result == actual_result

# @pytest.mark.code
# def test_input_98600_50():
#     input1 = 98600.50
#     input2 = 19720.10
#     expected_result = 328.67
#     actual_result = calculate_monthly_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.code
# def test_input_98991():
#     input1 = 98991
#     input2 = 19798.20
#     expected_result = 329.97
#     actual_result = calculate_monthly_payment(input1, input2)
#     assert expected_result == actual_result

# validate
# @pytest.mark.validate
# def test_int_input_150000():
#     input1 = 150000
#     input2 = 30000
#     expected_result = (150000,30000)
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_float_input_150000_50():
#     input1 = 150000.50
#     input2 = 30000.10
#     expected_result = (150000.50,30000.10)
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result    

# @pytest.mark.validate
# def test_zero_input():
#     input1 = 0
#     input2 = 0
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_zero_int_input():
#     input1 = 0
#     input2 = 30000
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be 20 percent of the price"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_zero_float_input():
#     input1 = 0
#     input2 = 30000.30
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be 20 percent of the price"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_int_zero_input():
#     input1 = 500000
#     input2 = 0
#     expected_result = "Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_float_zero_input():
#     input1 = 500000.30
#     input2 = 0
#     expected_result = "Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_negative_input():
#     input1 = -1
#     input2 = -1
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_negative_zero_input():
#     input1 = -1
#     input2 = 0
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_zero_negative_input():
#     input1 = 0
#     input2 = -1
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_negative_float_input():
#     input1 = -1.5
#     input2 = -1.5
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

@pytest.mark.validate
def test_negative_float_zero_input():
    input1 = -1.5
    input2 = 0
    expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"
    actual_result = validate_price_and_down_payment(input1, input2)
    assert expected_result == actual_result

# @pytest.mark.validate
# def test_zero_negative_float_input():
#     input1 = 0
#     input2 = -1.5
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_negative_float_int_input():
#     input1 = -1.5
#     input2 = 30000
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be 20 percent of the price"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_int_negative_float_input():
#     input1 = 30000
#     input2 = -1.5
#     expected_result = "Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

@pytest.mark.validate
def test_str_str_input():
    input1 = 'abc'
    input2 = 'abc'
    expected_result = "Error: Price must be a number and Error: Down payment must be a number"
    actual_result = validate_price_and_down_payment(input1, input2)
    assert expected_result == actual_result

# @pytest.mark.validate
# def test_int_str_input():
#     input1 = 300000
#     input2 = 'abc'
#     expected_result = "Error: Down payment must be a number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_str_int_input():
#     input1 = 'abc'
#     input2 = 300000
#     expected_result = "Error: Price must be a number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_float_str_input():
#     input1 = 300000.75
#     input2 = 'abc'
#     expected_result = "Error: Down payment must be a number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_str_float_input():
#     input1 = 'abc'
#     input2 = 300000.75
#     expected_result = "Error: Price must be a number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_str_zero_input():
#     input1 = 'abc'
#     input2 = 0
#     expected_result = "Error: Price must be a number and Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_zero_str_input():
#     input1 = 0
#     input2 = 'abc'
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be a number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_str_negative_input():
#     input1 = 'abc'
#     input2 = -1
#     expected_result = "Error: Price must be a number and Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_negative_str_input():
#     input1 = -1
#     input2 = 'abc'
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be a number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_str_negative_float_input():
#     input1 = 'abc'
#     input2 = -1.5
#     expected_result = "Error: Price must be a number and Error: Down payment must be a positive non-zero number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result

# @pytest.mark.validate
# def test_negative_float_str_input():
#     input1 = -1.5
#     input2 = 'abc'
#     expected_result = "Error: Price must be a positive non-zero number and Error: Down payment must be a number"
#     actual_result = validate_price_and_down_payment(input1, input2)
#     assert expected_result == actual_result


