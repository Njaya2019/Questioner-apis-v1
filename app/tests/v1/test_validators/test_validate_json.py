import pytest
from app.api.v1.validators.validate_json import validate_json_values
"""""""tests validate json class method"""""""
def test_validate_json_string_value():
    value1=validate_json_values.validate_json_string_value("HTML CSS AND JAVASCRIPT")
    value2=validate_json_values.validate_json_string_value(200)
    assert value1==True
    assert value2==False