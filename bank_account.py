import bcrypt
from response import Response


class BankAccount:
    ACCOUNT_BALANCE = "Account balance"
    MEMBERSHIP_NUM = "Membership number"
    PIN = "Pin number"
    MEMBER_NAME = "Member name"

    def __init__(self, account_balance, membership_num, pin, member_name):

        BankAccount._validate_float(BankAccount.ACCOUNT_BALANCE, account_balance)
        self._account_balance = account_balance

        BankAccount._validate_int(BankAccount.MEMBERSHIP_NUM, membership_num)
        self._membership_num = membership_num

        BankAccount._validate_int(BankAccount.PIN, pin)
        self._pin = bcrypt.hashpw(pin, bcrypt.gensalt())

        BankAccount._validate_str(BankAccount.MEMBER_NAME, member_name)
        self._member_name = member_name

    def validate_account(self, input_pin):
        return NotImplementedError

    def get_balance(self):
        return self._account_balance


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