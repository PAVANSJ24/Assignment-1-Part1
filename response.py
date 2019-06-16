from transaction import Transaction


class Response(Transaction):

    RESPONSE_ACCOUNT_BALANCE= "Account balance"
    RESPONSE_MEMBERSHIP_NUM= "Membership number"

    def __init__(self, date_time, token):
        super().__init__(date_time, token)
        self._input = input




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
        elif float_value < 0.0 :
            raise ValueError(display_name + " cannot be negative")

    @staticmethod
    def _validate_int(display_name, int_value):
        """ Check if the number is less than 0"""
        if int_value == None or type(int_value) != int:
            raise ValueError(display_name + " must be a valid integer value")
        elif int_value < 0.0:
            raise ValueError(display_name + " cannot be negative")