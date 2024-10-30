from bankaccouts import bank_account
import random

#contains failsafes for invalid requests

name = input("To create an account, please enter a name: ")
account_number = random.randint(100000, 999999)


cuenta = bank_account(account_number,name)
print(f"congratulations for creating your account, your account number is: {account_number}")


cuenta.check_balance()

cuenta.deposit()

cuenta.withdraw()

cuenta.check_balance()