from datetime import datetime
from src.exceptions import WithdrawalTimeRestrictionError

class BankAccount:
    def __init__(self, balance=0,log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction("Cuenta creada")

    def _log_transaction(self,message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")
     
    def deposit(self, amount=0):
        if amount>0:
            self.balance+=amount
            self._log_transaction(f"Se deposito {amount}, nuevo balance: {self.balance}")
        else:
            raise ValueError ("Se debe depositar un valor mayor a 0")
        return self.balance
    
    def withdraw(self, amount=0):
        now = datetime.now()
        if now.hour < 8 or now.hour > 17:
            raise WithdrawalTimeRestrictionError("Withdrawal are only allowed between 8 and 17")
        if amount > self.balance:
            self._log_transaction(f"Intento retirno: Fondos Insuficientes")
            raise ValueError ("No hay fondos suficientes")
        elif amount>0:
            self.balance-=amount
            self._log_transaction(f"Se retiró {amount}, nuevo balance: {self.balance}")
        else:
            raise ValueError ("Se debe retirar un valor mayor a 0")
        return self.balance
    
    def get_balance(self):
        return self.balance