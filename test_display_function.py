from function import display_month
import pytest

@pytest.mark.display
@pytest.mark.parametrize('input_number,expected_result', [ 
    (1,"January"), (2,"February"), (3,"March"), (4,"April"), (5,"May"), (6,"June"), 
              (7,"July"), (8,"August"), (9,"September"), (10,"October"), (11,"November"), (12,"December"),
              (0,"Error: Month number out of range"),(13,"Error: Month number out of range"),(-10,"Error: Month number out of range"),
              (22,"Error: Month number out of range"),(1.1,"Error: Please input integer"),(13.1,"Error: Month number out of range"),
              ("a","Error: Please input integer"),("#","Error: Please input integer"),(0.5,"Error: Month number out of range"),
              (1.5,"Error: Please input integer"),(-1.5,"Error: Month number out of range")
])
def test_display(input_number, expected_result):
    actual_result =  display_month(input_number)
    assert expected_result == actual_result
