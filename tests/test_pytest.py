import pytest
from src.bank_account import BankAccount

@pytest.mark.parametrize("amount,expected",[
    (100,1100),
    (3000,4000),
    (4500,5500),
])
def test_deposit_varios_amounts(amount,expected):

    account = BankAccount(balance=1000,log_file="transaction_log.txt")
    new_balance = account.deposit(amount)
    
    assert new_balance == expected

def test_sum():
    a= 4
    b=8
    assert a+b == 12

def test_deposit_negative():
    account = BankAccount(balance=1000,log_file="transaction_log.txt")
    with pytest.raises(ValueError):
        account.deposit(-100)
