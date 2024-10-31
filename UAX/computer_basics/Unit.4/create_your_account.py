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
