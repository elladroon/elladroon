from bankaccouts import bank_account
import random

#contains failsafes for invalid requests

name = input("To create an account, please enter a name: ")
account_number = random.randint(100000, 999999)


cuenta = bank_account(account_number,name)
print("---------------------------------------------------------------")
print(f"congratulations for creating your account, your info is the following: ")

print(cuenta)
print("---------------------------------------------------------------")

cuenta.deposit()

cuenta.withdraw()

cuenta.check_balance()


"""
class savings_acc(bank_account):
    def __init__(self,interest_rate = 5 ,inter_generated = 0):
        super().__init__(account_number, name)
        self.interest_rate = interest_rate
        self.inter_generated = inter_generated
    
    def calculate_interest(self):
        self.inter_generated = self.balance * self.interest_rate / 100
"""
