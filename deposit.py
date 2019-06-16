from transaction import Transaction
from response import Response


class Deposit(Transaction):
    def __init__(self, deposit_amount, date_time, token, account_balance, membership_num):
        super().__init__(date_time, token, date_time, token, account_balance, membership_num)
        self._deposit_amount = deposit_amount
        self._date_time = date_time
        self._account_balance = account_balance

    def deposit(self, amount):

        if self._deposit_amount > 0:
            self._account_balance += self._deposit_amount
            Response("Deposit Complete")
        else:
            return "Deposit must be higher than 0"


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