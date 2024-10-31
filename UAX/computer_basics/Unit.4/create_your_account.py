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
print("")

im = 0
while True:

    while im < 1 or im > 4:
        im = int(input("To deposi enter 1, to withdraw enter 2, to check your check information enter 3, to exit 4: "))
        if im < 1 or im > 4:
            print("---------------------------------------------------------------")
            print("Invalid input, please enter a number between 1 and 4.")
            print("---------------------------------------------------------------")

    if im == 1:
        cuenta.deposit()
        im = 0
    elif im == 2:
        cuenta.withdraw()
        im = 0
    elif im ==3:
        cuenta.check_balance()
        im = 0
    elif im == 4:
        break

print("by")
"""
class savings_acc(bank_account):
    def __init__(self,interest_rate = 5 ,inter_generated = 0):
        super().__init__(account_number, name)
        self.interest_rate = interest_rate
        self.inter_generated = inter_generated
    
    def calculate_interest(self):
        self.inter_generated = self.balance * self.interest_rate / 100
"""
