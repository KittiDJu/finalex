from function import display_monthly_payment, validate_price
import pytest

@pytest.mark.display
@pytest.mark.parametrize('input_number,expected_result', [ 
    (150000,500),
    (150000.50,500.00),
    (0,"Error: Please input positive integer or float price"), 
    (-1,"Error: Price must be a positive non-zero number"),
    (-1.5,"Error: Price must be a positive non-zero number"), 
    ("a","Error: Please input positive integer or float price"), 
    ("&","Error: Please input positive integer or float price")
])
def test_display_monthly(input_number, expected_result):
    actual_result =  display_monthly_payment(input_number)
    assert expected_result == actual_result

# @pytest.mark.display
# @pytest.mark.parametrize('input_number,expected_result', [ 
#     (150000, 30000),
#     (150000.50, 30000.10)  
# ])
# def test_display_down(input_number, expected_result):
#     actual_result =  display_down_payment(input_number)
#     assert expected_result == actual_result

