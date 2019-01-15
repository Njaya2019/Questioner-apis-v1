import re
#A class to validate json values

class validate_json_values():
    @classmethod
    def validate_json_string_value(cls,json_value):
        """
        Class method checks if json value is actually a string and 
        returns a boolean
        """
        if type(json_value)==int:
            return False     
        else:
            return True

    @classmethod
    def validate_json_integer_value(cls,json_value):
        """Class method checks if json value is actually an interger
         and returns a boolean True else false
         """
        if type(json_value)==int:
            return True    
        else:
            return False
            
    @classmethod
    def validate_json_email_value(cls,json_value):
        """Class method to check if the email is valid returns true
         if it is else false.
         Below is a regular expression to match an email.
         """
        pattern=re.compile(r"[a-zA-Z0-9]+@[a-zA-Z]+\.com")
        matches=pattern.finditer(json_value)
        for match in matches:
            if match:
                return True
        return False