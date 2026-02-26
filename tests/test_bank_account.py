import unittest
import os
from unittest.mock import patch
from src.bank_account import BankAccount
from src.exceptions import WithdrawalTimeRestrictionError

class BankAccountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000,log_file="transaction_log.txt")
    
    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self,filename):
        with open(filename,"r") as f:
            return len(f.readlines())

    def test_deposit(self):
        #account = BankAccount(balance=1000)
        new_balance = self.account.deposit(500)
        #assert new_balance == 1500
        self.assertEqual(new_balance,1500,"El balance no es igual a lo esperado")
        
    def test_deposit_error(self):
        with self.assertRaises(ValueError):
            self.account.deposit()

    @patch("src.bank_account.datetime")
    def test_withdraw(self,mock_datetime):
        mock_datetime.now.return_value.hour = 10
        #account = BankAccount(balance=1000)
        new_balance = self.account.withdraw(500)
        #assert new_balance == 500
        self.assertEqual(new_balance,500,"El balance no es igual a lo esperado")

    @patch("src.bank_account.datetime")
    def test_withDraw_error(self,mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(ValueError):
            self.account.withdraw()
    
    @patch("src.bank_account.datetime")
    def test_withDraw_noFondos(self,mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(ValueError):
            self.account.withdraw(1500)

    @patch("src.bank_account.datetime")
    def test_withDraw_noFondos_message(self,mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(ValueError) as context:
            self.account.withdraw(1500)
        self.assertEqual(str(context.exception), "No hay fondos suficientes")

    def test_get_balance(self):
        #account = BankAccount(balance=1000)
        #assert self.account.get_balance() == 1000
        self.assertEqual(self.account.get_balance(),1000,"El balance no es igual a lo esperado")

    def test_transaction_log(self):
        self.account.deposit(500)
        #assert os.path.exists("transaction_log.txt")
        self.assertTrue(os.path.exists("transaction_log.txt"))

    @patch("src.bank_account.datetime")
    def test_count_transactions(self,mock_datetime):
        mock_datetime.now.return_value.hour = 11
        assert self._count_lines(self.account.log_file) ==1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) ==2
        with self.assertRaises(ValueError):
            self.account.deposit()
        assert self._count_lines(self.account.log_file) ==2
        with self.assertRaises(ValueError):
            self.account.withdraw(2500)
        assert self._count_lines(self.account.log_file) ==3

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 11
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance,900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)
    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 5
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    def test_deposit_varios_amounts(self):
        test_cases = [
            {"amount":100,"expected":1100},
            {"amount":3000,"expected":4000},
            {"amount":4500,"expected":5500}
        ]
        for case in test_cases:
            with self.subTest(case = case):
                self.account = BankAccount(balance=1000,log_file="transaction_log.txt")
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])