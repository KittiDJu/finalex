from function import display_monthly_payment
import pytest

@pytest.mark.display
@pytest.mark.parametrize('input_number1, input_number2, expected_result', [
    # Normal cases
    # (150000, 30000, 500.00),
    # (98600.50, 19720.10, 328.67),
    # (98991, 19798.20, 329.97),

    # Error cases
    # (0, 0, "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"),
    # (0, 30000, "Error: Price must be a positive non-zero number and Error: Down payment must be 20 percent of the price"),
    # (0, 30000.30, "Error: Price must be a positive non-zero number and Error: Down payment must be 20 percent of the price"),
    # (500000, 0, "Error: Down payment must be a positive non-zero number"),
    # (500000.30, 0, "Error: Down payment must be a positive non-zero number"),
    # (-1, -1, "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"),
    # (-1, 0, "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"),
    # (0, -1, "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"),
    # (-1.5, -1.5, "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"),
    # (-1.5, 0, "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"),
    # (0, -1.5, "Error: Price must be a positive non-zero number and Error: Down payment must be a positive non-zero number"),
    # (-1.5, 30000, "Error: Price must be a positive non-zero number and Error: Down payment must be 20 percent of the price"),
    # (30000, -1.5, "Error: Down payment must be a positive non-zero number"),
    # ("abc", "abc", "Error: Price must be a number and Error: Down payment must be a number"),
    # (300000, "abc", "Error: Down payment must be a number"),
    # ("abc", 300000, "Error: Price must be a number"),
    # (300000.75, "abc", "Error: Down payment must be a number"),
    # ("abc", 300000.75, "Error: Price must be a number"),
    # ("abc", 0, "Error: Price must be a number and Error: Down payment must be a positive non-zero number"),
    # (0, "abc", "Error: Price must be a positive non-zero number and Error: Down payment must be a number"),
    # ("abc", -1, "Error: Price must be a number and Error: Down payment must be a positive non-zero number"),
    # (-1, "abc", "Error: Price must be a positive non-zero number and Error: Down payment must be a number"),
    # ("abc", -1.5, "Error: Price must be a number and Error: Down payment must be a positive non-zero number"),
    # (-1.5, "abc", "Error: Price must be a positive non-zero number and Error: Down payment must be a number"),
])
def test_display_monthly(input_number1, input_number2, expected_result):
    actual_result =  display_monthly_payment(input_number1, input_number2)
    assert expected_result == actual_result