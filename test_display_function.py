from function import display_month
import pytest

@pytest.mark.display
@pytest.mark.parametrize('input_number,expected_result', [ 
    (150000,500), (150000.50,500.001666667), (0,"Error: Price must be a positive non-zero number"), (-1,"Error: Price must be a positive non-zero number"1)
    (-1.5,"Error: Price must be a positive non-zero number"), ("a","Error: Please input integer or float price"), 
    ("&","Error: Please input integer or float price")
])
def test_display(input_number, expected_result):
    actual_result =  display_monthly(input_number)
    assert expected_result == actual_result
