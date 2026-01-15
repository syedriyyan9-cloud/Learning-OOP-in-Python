"""Module For Bank"""

from accounts import Accounts

class Bank:
    """A class to represent Bank"""

    def __init__(self):
        """initialize attributes of bank"""
        self.accounts = {}
        self.account_number = 0

    def create_account(self, name, password, balance):
        """Create an account for user"""
        print()
        account = Accounts(name,password,balance)
        self.accounts[self.account_number] = account
        print("User created successfully")
        print(f"Your Account Number is: {self.account_number}")
        self.account_number += 1
        print()

    def open_account(self):
        """Open user account"""
        print()
        name = input("What is your name?")
        password = input("What is your password?")
        balance = int(input("How much balance do you want to enter? $:"))
        self.create_account(name,password,balance)
        print()

    def withdraw(self):
        """Method for withdrawing balance"""
        print()
        acc_num = int(input("What is your account number: "))
        user = self.accounts.get(acc_num)
        if user:
            password = input("What is your password?")
            balance = int(input("Enter the amount you want to withdraw"))
            user.withdraw(password,balance)
            print()
        else:
            print(f"No such user with {acc_num} exits.")
            print()
        print()

    def deposit(self):
        """Method for depositing balance"""
        print()
        acc_num = int(input("What is your account number: "))
        user = self.accounts.get(acc_num)
        if user:
            password = input("What is your password?")
            balance = int(input("Enter the amount you want to deposit"))
            user.deposit(password,balance)
            print()
        else:
            print(f"No such user with {acc_num} exits.")
            print()
        print()
    
    def show_single_user(self):
        """Method to display details for single user"""
        print()
        acc_num = int(input("What is your account number: "))
        user = self.accounts.get(acc_num)
        if user:
            user.check()
            print()
        else:
            print(f"No such user exits")
            print()
        print()

    def show_all_users(self):
        """Method to show all users"""
        print()
        for account in self.accounts:
            print(f"{self.accounts[account].check()}")
            print(f"Account Number: {account}")
            print()
        print()

    def delete_account(self):
        """Method to delete accounts"""
        print()
        acc_num = int(input("What is your account number: "))
        user = self.accounts.get(acc_num)
        if user:
            del self.accounts[acc_num]
            print("User Deleted")
            print()
        else:
            print("No such user existed")
            print()
        print()
