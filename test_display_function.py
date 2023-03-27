from function import display_month
import pytest

@pytest.mark.display
@pytest.mark.parametrize('input_number,expected_result', [ 
    (150000,500), (,40000),
])
def test_display(input_number, expected_result):
    actual_result =  display_month(input_number)
    assert expected_result == actual_result
