from function import number_to_month,validate_number
import pytest
#pytest -m code
@pytest.mark.code
def test_January_input_1():
    input = 1
    expected_result = "January"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_Fabruary_input_2():
    input = 2
    expected_result = "February"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_March_input_3():
    input = 3
    expected_result = "March"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_April_input_4():
    input = 4
    expected_result = "April"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_May_input_5():
    input = 5
    expected_result = "May"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_June_input_6():
    input = 6
    expected_result = "June"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_July_input_7():
    input = 7
    expected_result = "July"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_August_input_8():
    input = 8
    expected_result = "August"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_September_input_9():
    input = 9
    expected_result = "September"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_October_input_10():
    input = 10
    expected_result = "October"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_November_input_11():
    input = 11
    expected_result = "November"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

@pytest.mark.code
def test_December_input_12():
    input = 12
    expected_result = "December"
    actual_result = number_to_month(input)
    assert expected_result == actual_result

#pytest -m validate
@pytest.mark.validate
def test_out_of_range_input_0():
    input = 0
    expected_result = "Error: Month number out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_out_of_range_input_13():
    input = 13
    expected_result = "Error: Month number out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_out_of_range_input_minus_10():
    input = -10
    expected_result = "Error: Month number out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_out_of_range_input_22():
    input = 22
    expected_result = "Error: Month number out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_integer_input_1_p_1():
    input = 1.1
    expected_result = "Error: Please input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_integer_input_13_p_1():
    input = 13.1
    expected_result = "Error: Month number out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_str_input_a():
    input = "a"
    expected_result = "Error: Please input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_integer_input_charp():
    input = "#"
    expected_result = "Error: Please input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_integer_input_1():
    input = 1
    expected_result = 1
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_integer_input_12():
    input = 12
    expected_result = 12
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_integer_input_0_p_5():
    input = 0.5
    expected_result = "Error: Month number out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_integer_input_m_1_p_5():
    input = -1.5
    expected_result = "Error: Month number out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result

@pytest.mark.validate
def test_integer_input_1_p_5():
    input = 1.5
    expected_result = "Error: Please input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result







