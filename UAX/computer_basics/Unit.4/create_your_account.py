from bankaccouts import bank_account
import random
#------------------------------------------------------------------------------
#contains failsafes for invalid requests
#------------------------------------------------------------------------------



class savings_acc(bank_account):
    def __init__(self, account_number, name, interest_rate=5, inter_generated=0, balance=0):
        super().__init__(account_number, name, balance)
        self.interest_rate = interest_rate
        self.inter_generated = inter_generated
    
    def calculate_interest(self):
        self.inter_generated = self.balance * self.interest_rate / 100


class checking_acc(bank_account):
    def __init__(self, account_number, name, interest_rate=5, inter_generated=0, balance=0):
        super().__init__(account_number, name, balance)
        self.interest_rate = interest_rate
        self.inter_generated = inter_generated
    
    def overdraft_lim(self):
        pass
#------------------------------------------------------------------------------



def account_created(cuenta):
    print("congratulations for creating your account, your info is the following: ")
    print(cuenta)
    print("---------------------------------------------------------------")
    print("")


def welcome(name):
    which = input("to create a bank account introduce 1, to create a savings account introduce 2, to create a checkig account introduce 3: ")
    salir = ""

    if which == '1':
        account_number = random.randint(100000, 999999)
        acc = bank_account(account_number,name)
        account_created(acc)
        tipo_cuenta =  acc
        
        
    elif which == '2':
        account2_number = random.randint(100000, 999999)
        sv_acc = savings_acc(account2_number,name)
        account_created(sv_acc)   
        tipo_cuenta =  sv_acc


    elif which == '3':
        account3_number = random.randint(100000, 999999)
        check_acc = checking_acc(account3_number,name)
        account_created(check_acc)   
        tipo_cuenta =  check_acc


    else:
        print("Invalid input, please enter a number between 1 and 4.")
        welcome(name)


    

    while True:

        im = int(input("To deposit enter 1, to withdraw enter 2, to check your information enter 3, to exit 4: "))
            
        if im == 1:
            tipo_cuenta.deposit()
            
        elif im == 2:
            tipo_cuenta.withdraw()
            
        elif im ==3:
            print(tipo_cuenta)

        elif im == 4:
            while True:
                salir = input("would you like to create another account? (y/n): ")
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
            
        
        if salir == "n":
            break


#------------------------------------------------------------------------------


print("Welcome")
name = input("To create an account, please enter a name: ")
print("----------------------------------------------------------------")
print("")
print(f"hi {name}")
welcome(name)
