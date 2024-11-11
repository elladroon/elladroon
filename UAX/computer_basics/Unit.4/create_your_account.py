from bankaccouts import bank_account  # Importing the bank_account class from bankaccouts module
import random  # Importing random for generating account numbers

#------------------------------------------------------------------------------
# Contains failsafes for invalid requests
#------------------------------------------------------------------------------


# Defining a class for Savings Accounts that inherits from bank_account
class savings_acc(bank_account):
    def __init__(self, account_number, name, interest_rate=5, inter_generated=0, balance=0):
        super().__init__(account_number, name, balance)  # Initializing the base class
        self.interest_rate = interest_rate  # Default interest rate for savings account
        self.inter_generated = inter_generated  # Initial interest generated set to 0

    # Method to calculate interest based on current balance and interest rate
    def calculate_interest(self):
        self.inter_generated = self.balance * self.interest_rate / 100
        return self.inter_generated

    # String representation of the savings account details
    def __str__(self):
        return "Account Number (savings acc): " + str(self.account_number) + \
               ",  Account Holder Name: " + str(self.account_holder_name) + \
               ",  Balance: " + str(self.balance) + \
               ", interest rate per month: " + str(self.interest_rate)

    # Method to calculate expected earnings over a user-defined time period
    def interes_time(self):
        print("current interest rate: " + str(self.interest_rate))
        time = int(input("Introduce the time in months to calculate the expected earnings: "))
        total = time * self.balance * self.interest_rate / 100
        print(f" The expected earnings are: {total}")


# Defining a class for Checking Accounts that inherits from bank_account
class checking_acc(bank_account):
    def __init__(self, account_number, name, interest_rate=5, inter_generated=0, balance=0, overdraft=200):
        super().__init__(account_number, name, balance)  # Initializing the base class
        self.interest_rate = interest_rate  # Interest rate, if applicable
        self.inter_generated = inter_generated  # Initial interest generated set to 0
        self.overdraft = overdraft  # Default overdraft limit for checking accounts

    # Method to withdraw from the account with overdraft protection
    def withdraw(self):
        amount = float(input("Introduce the amount to withdraw: "))
        if amount > self.balance + self.overdraft:  # Checking if amount exceeds balance + overdraft
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Your new balance is: {self.balance}")

    # String representation of the checking account details
    def __str__(self):
        return "Account Number (check acc): " + str(self.account_number) + \
               ",  Account Holder Name: " + str(self.account_holder_name) + \
               ",  Balance: " + str(self.balance) + \
               ", overdraft: " + str(self.overdraft)

#------------------------------------------------------------------------------


# Function to display account creation details
def account_created(cuenta):
    print("Congratulations for creating your account, your info is the following: ")
    print(cuenta)
    print("---------------------------------------------------------------")
    print("")


# Function to guide the user through account creation process and banking operations
def welcome(name):
    # Prompt user to choose an account type
    which = input("To create a bank account introduce 1, to create a savings account introduce 2, to create a checking account introduce 3: ")
    salir = ""

    # Based on user input, create the corresponding account type
    if which == '1':
        account_number = random.randint(100000, 999999)
        acc = bank_account(account_number, name)
        account_created(acc)
        tipo_cuenta = acc

    elif which == '2':
        account2_number = random.randint(100000, 999999)
        sv_acc = savings_acc(account2_number, name)
        account_created(sv_acc)
        tipo_cuenta = sv_acc

    elif which == '3':
        account3_number = random.randint(100000, 999999)
        check_acc = checking_acc(account3_number, name)
        account_created(check_acc)
        tipo_cuenta = check_acc

    else:
        print("Invalid input, please enter a number between 1 and 3.")
        welcome(name)  # Recursive call if input is invalid

    # Loop to allow user to perform banking operations on their account
    while True:
        if which == "2":  # If Savings Account
            im = int(input("To deposit enter 1, to withdraw enter 2, to check your information enter 3, to see expected earnings 4, to exit 0: "))
        else:  # For other account types
            im = int(input("To deposit enter 1, to withdraw enter 2, to check your information enter 3, to exit 0: "))

        # Perform actions based on user's choice
        if im == 1:
            tipo_cuenta.deposit()

        elif im == 2:
            tipo_cuenta.withdraw()

        elif im == 3:
            print("-------------------------------------------------")
            print(tipo_cuenta)
            print("-------------------------------------------------")

        elif im == 4 and which == "2":
            tipo_cuenta.interes_time()

        elif im == 0:
            # Option to create another account after exiting
            while True:
                salir = input("Would you like to create another account? (y/n): ")
                if salir == 'y':
                    welcome(name)
                elif salir == "n":
                    print("Thank you for using our banking system")
                    break
                else:
                    print("Invalid input, please enter a 'y' or 'n'.")

        else:
            print("---------------------------------------------------------------")
            print("Invalid input, please enter a number between 1 and 4.")
            print("---------------------------------------------------------------")

        # Exit if user chooses not to create another account
        if salir == "n":
            print("")
            break


#------------------------------------------------------------------------------


# Entry point of the banking system program
print("Welcome")
name = input("To create an account, please enter a name: ")
print("----------------------------------------------------------------")
print("")
print(f"Hi {name}")
welcome(name)  # Call the welcome function with user's name


