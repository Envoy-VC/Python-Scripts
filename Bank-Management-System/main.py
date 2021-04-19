import pickle
import random


def create_account():
    account = {}
    a = True
    account_number = random.randrange(100000,999999)
    account_holder_name = str(input("Enter Name of Account Holder - "))
    while a:
        account_type = str(input("Enter type of Account(C/S) - "))
        if account_type.lower() != 'c' and account_type.lower() != 's':
            print("UNDEFINED ACCOUNT TYPE")
        if account_type.lower() == 'c' or account_type.lower() == 's':
            a = False
    initial_amount = int(input("Enter Initial Amount - "))
    print(f"\n\nAccount Created Successfully\nAccount Number - {account_number}\n")
    account['account_number'] = account_number
    account['account_holder_name'] = account_holder_name
    account['account_type'] = account_type.upper()
    account['initial_amount'] = initial_amount
    with open("account.dat","ab") as f:
        pickle.dump(account,f)

def display_all_accounts():
    accounts = {}
    file = open('account.dat', 'rb')
    try:
        while True:
            accounts = pickle.load(file)
            print(f"\n{accounts}\n")
    except EOFError:
        file.close()

def display_account_details():
    account_number = int(input("Enter Account Number - "))
    account = {}
    with open('account.dat','rb') as f:
        try:
            while True:
                account = pickle.load(f)
                if account['account_number'] == account_number:
                    print(f"\nAccount Number = {account['account_number']}\nAccount Holder = {account['account_holder_name']}\nAccount Type = {account['account_type']}\nAmount = {account['initial_amount']}\n\n")
        except EOFError:
            f.close()


def deposit_withdraw():
    account_number = int(input("Enter Account Number - "))
    choice = int(input(f"1.Deposit\n2.Withdraw\n\nEnter Choice - "))
    account = {}
    found = False
    if choice == 1:
        deposit = int(input("Enter Amount to be Deposited - "))
        with open('account.dat', 'rb+') as f:
            try:
                while True:
                    location = f.tell()
                    account = pickle.load(f)
                    if account['account_number'] == account_number:
                        account['initial_amount'] += deposit
                        f.seek(location)
                        pickle.dump(account,f)

            except EOFError:
                f.close()

    if choice == 2:
        withdraw = int(input("Enter Amount to Withdraw - "))
        with open('account.dat', 'rb+') as f:
            try:
                while True:
                    location = f.tell()
                    account = pickle.load(f)
                    if account['account_number'] == account_number:
                        account['initial_amount'] -= withdraw
                        f.seek(location)
                        pickle.dump(account,f)

            except EOFError:
                f.close()

def modify_account():
    account_number = int(input("Enter Account Number - "))
    account = {}
    with open('account.dat', 'rb+') as f:
        try:
            while True:
                location = f.tell()
                account = pickle.load(f)
                if account['account_number'] == account_number:
                    a = True
                    name = str(input("Enter Account Holder Name - "))
                    while a:
                        type = str(input("Enter type of Account(C/S) - "))
                        if type.lower() != 'c' and type.lower() != 's':
                            print("UNDEFINED ACCOUNT TYPE")
                        if type.lower() == 'c' or type.lower() == 's':
                            a = False
                    account['account_holder_name'] = name
                    account['account_type'] = type.upper()
                    f.seek(location)
                    pickle.dump(account,f)
        except EOFError:
            f.close()

if __name__ == '__main__':
    print("""
========================================================
                BANK MANAGEMENT SYSTEM
========================================================
    """)
    running = True
    while running:
        choice = int(input(f"Enter your Choice:\n1.Create Account\n2.Display All Accounts\n3.Display Your Account\n4.Deposit (or) Withdraw\n5.Modify Account\n6.Exit\n\nEnter your choice(1~6) - "))
        if choice == 1:
            create_account()
        elif choice == 2:
            display_all_accounts()
        elif choice == 3:
            display_account_details()
        elif choice == 4:
            deposit_withdraw()
        elif choice == 5:
            modify_account()
        elif choice == 6:
            running = False
        else:
            print("Wrong Choice")
