"""""""A class to validate json values"""""""

class validate_json_values():
    """""""Class method checks if json value is actually a string and returns a boolean"""""""
    @classmethod
    def validate_json_string_value(cls,json_value):
        if type(json_value)==int:
            return False     
        else:
            return True
            
        
