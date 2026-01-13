"""Module for Running the Entire Program"""

from bank import *

def display():
    """show menu"""
    bank = Bank()
    while True:
        print("To Create account press: \'C\'")
        print("To Open account press: \'O\'")
        print("To Show account details press: \'S\'")
        print("To Show all accounts in bank press: \'SA\'")
        print("To Withdraw from account press: \'W\'")
        print("To Deposit to account press: \'D\'")
        print("To End (close) to account press: \'E\'")
        print("To Quit program press: \'Q\'")
        choice = input("Your Choice: ")
        if choice.lower() == 'c':
            name = input("What is your name?")
            password = input("What is your password?").lower()
            balance = int(input("How much balance do you want to enter? $:"))
            bank.create_account(name,password,balance)
        if choice.lower() == 'o':
            bank.open_account()
        if choice.lower() == 'w':
            bank.withdraw()
        if choice.lower() == 'd':
            bank.deposit()
        if choice.lower() == 's':
            bank.show_single_user()
        if choice.lower() == 'sa':
            bank.show_all_users()
        if choice.lower() == 'e':
            bank.delete_account()
        if choice.lower() == 'q':
            break

if __name__ == '__main__':
    display()


