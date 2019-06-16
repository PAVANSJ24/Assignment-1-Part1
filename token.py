import hashlib


class Token:
    """class for Token"""
    TOKEN_TOKEN_NUMBER= "Token number"
    TOKEN_PIN= "PIN"

    def __init__(self, token_number, pin):

        Token._validate_float(Token.TOKEN_TOKEN_NUMBER, token_number)
        self._token_number= token_number

        hash_object = hashlib.sha1(pin)
        hex_dig = hash_object.hexdigest()
        print(hex_dig)

        Token._validate_int(Token.TOKEN_PIN, pin)
        self._pin= pin










    @staticmethod
    def _validate_str(display_name, str_value):
        """ Check if the string is None or empty"""
        if str_value == None:
            raise ValueError(display_name + " cannot be none")
        elif str_value == "":
            raise ValueError(display_name + " cannot be empty")

    @staticmethod
    def _validate_float(display_name, float_value):
        """ Check if the number is less than 0"""
        if float_value == None or type(float_value) != float:
            raise ValueError(display_name + " must be a valid floating point value")
        elif float_value < 0.0:
            raise ValueError(display_name + " cannot be negative")

    @staticmethod
    def _validate_int(display_name, int_value):
        """ Check if the number is less than 0"""
        if int_value == None or type(int_value) != int:
            raise ValueError(display_name + " must be a valid integer value")
        elif int_value < 0.0:
            raise ValueError(display_name + " cannot be negative")