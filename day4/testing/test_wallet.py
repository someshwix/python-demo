#BDD
import pytest
from wallet import Wallet, InsufficientFunds
def test_initial_amount():
    wallet = Wallet(500)
    asserts wallet.balance == 500   

def test_addCash():
    wallet = Wallet(500)
    wallet.add_cash(500)
    assert wallet.balance == 1000         
    '''
class InsufficientFunds(Exception):
    pass

class Wallet(object):
    def __init__(self,initial_amount=0):
        self.balance=initial_amount

    def spend_cash(self,amount):
        if self.balance <amount:
            raise InsufficientFunds(f"Not enough amount available: {self.balance}")
        self.balance -=amount
    
    def add_cash(self,amount):
        self.balance += amount
        '''