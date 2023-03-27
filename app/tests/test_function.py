from function import number_to_month,validate_number
import pytest
#pytest -m code
@pytest.mark.code
def test_money_input_1():
    input = 1
    expected_result = "January"
    actual_result = number_to_month(input)
    assert expected_result == actual_result
