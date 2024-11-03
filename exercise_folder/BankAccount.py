#------Home Exerecise------#

import random
import string


class BankAccount():
    def __init__(self, first_name, last_name, address, initial_balance=0.0, currency='$'):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.account_number = self.generate_account_number()
        self.balance = initial_balance
        self.currency = currency

    def generate_account_number(self):
        return ''.join(random.choices(string.digits, k=10))
    
    
    def deposit(self, amount, currency='$'):
        self.currency != currency
        if amount > 0:
            self.balance += amount
            print(f'Deposited {amount}{self.currency} to your account!')
            return True
        else:
            print(f'Deposit most be greater than "0"!')
            return False

    def withdraw(self, amount, currency='$'):
        self.currency != currency
        if 0 < amount < self.balance:
            self.balance -= amount
            print(f'Withdrawn {amount}{self.currency} from your account!')
            return True
        else:
            print(f'Withdraw most be greater than "0" and your account balance!')
            return False

    def display_balance(self):
        print(f'Current balance: {self.balance}{self.currency}')
        print('---------------------------------------------------')        

    def display_account_details(self):
        print(f'Account holder: {self.first_name} {self.last_name}')
        print(f'Address: {self.address}')
        print(f'Account number: {self.account_number}')
        print(f'Current Balance: {self.balance}{self.currency}')                        


account = BankAccount('May', 'Elbaz', 'Tikva 6, Tel-Aviv, Israel')
account.display_account_details()
account.deposit(10000)
account.withdraw(250)
account.display_balance()

account = BankAccount('Eli', 'David', 'Hadar 1, Gan Yavne, Israel')
account.display_account_details()
account.deposit(2000)
account.withdraw(350.1)
account.display_balance()

account = BankAccount('Mor', 'Anavim', 'Tikcva 6, Mevaseret, Israel')
account.display_account_details()
account.deposit(200000)
account.withdraw(50000)
account.display_balance()
