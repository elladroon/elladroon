class bank_account:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def check_balance(self):
        print("---------------------------------------------------------------")  
        print(f"Your current balance is: {self.balance}")
        print("---------------------------------------------------------------")
        print("")

    def deposit(self):
        try:
            deposit = int(input(f"Hi {self.account_holder_name}, please introduce the cuantity to import: "))
            if  deposit < 0:
                    print(f"You can't deposit an ammount of {deposit}")
                    print("----------------------------------------------------------")  
                    bank_account.deposit(self)
            else:
                self.balance += deposit
                print(f"current balance: {self.balance}")
                print("")
        except:
            print("It seems like something went wrong, please enter a number")
            print("----------------------------------------------------------")    
            bank_account.deposit(self)

    def withdraw(self):
        try:
            withdraw = int(input(f"Hi {self.account_holder_name}, please introduce the cuantity to withdraw: "))
            if withdraw < 0:
                print("You can't withdraw that amount")
                print("----------------------------------------------------------")  
                bank_account.withdraw(self)
            else:
                if self.balance < withdraw:
                    print(f"your current balance is {self.balance}, you cant withdraw that quantity")
                    print("----------------------------------------------------------")  
                    bank_account.withdraw(self)
                else:    
                    self.balance -= withdraw 
                    print(f"current balance: {self.balance}")   
                    print("")       
        except:
            print("It seems like something went wrong, please enter a number")   
            print("----------------------------------------------------------")   
            bank_account.withdraw(self)


# ----------------------- quitar esto luego -----------------------

# import bank account from bankaccounts
# print("please introduce the following data to create a bank account")
# name 

"""
bank1 = bank_account(12345, "pepe")

bank1.deposit()

bank1.withdraw()

bank1.check_balance()"""
