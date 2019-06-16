import datetime
from deposit import Deposit
from withdraw import Withdraw
from checkbalance import CheckBalance
from bank_account import BankAccount


class Transaction(BankAccount):
    """class for the Transaction"""

    TRANSACTION_DATETIME = "Datetime"
    TRANSACTION_TOKEN = "Token"

    def __init__(self, date_time, token, account_balance, membership_num, pin, member_name):
        super().__init__(account_balance, membership_num, pin, member_name)
        Transaction._validate_str(Transaction.TRANSACTION_DATETIME, date_time)
        self._date_time = date_time
        Transaction._validate_int(Transaction.TRANSACTION_TOKEN, token)
        self._token = token

    def get_date_time(self):
        """get the date in format of yyyy/mm/dd hh:mm"""
        formatted_datetime = datetime.datetime.strptime(self._date_time, "%Y-%m-%d %H:%M:%S.%f")
        return formatted_datetime.strftime("%Y-%m-%d %H:%M:%S.%f")

    def deposit(self, amount):
        """get deposit amount of account"""
        Deposit(amount, self._date_time, self._token)

    def withdraw(self, amount):
        """get withdraw amount of account"""
        Withdraw(amount, self._date_time, self._token)

    def checkbalance(self):
        """get balance of account"""
        CheckBalance


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