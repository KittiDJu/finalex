from function import display_monthly_payment
import pytest

@pytest.mark.display
@pytest.mark.parametrize('input_number1, input_number2, expected_result', [ 
    (150000,30000,500.0),
])
def test_display_monthly(input_number1, input_number2, expected_result):
    actual_result =  display_monthly_payment(input_number1, input_number2)
    assert expected_result == actual_result