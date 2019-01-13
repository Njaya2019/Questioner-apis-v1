import pytest
from validators.validate_json import validate_json_values
"""""""tests validate json class method"""""""
def test_validate_json_string_value():
    value1=validate_json_values.validate_json_string_value("HTML CSS AND JAVASCRIPT")
    value2=validate_json_values.validate_json_string_value(200)
    assert value1==True
    assert value2==False

def test_validate_json_email_value():
    correct_email=validate_json_values.validate_json_email_value("njayaandrew@gmail.com")
    wrong_email=validate_json_values.validate_json_email_value("AntonyOboregmail.com")
    assert correct_email==True
    assert wrong_email==False