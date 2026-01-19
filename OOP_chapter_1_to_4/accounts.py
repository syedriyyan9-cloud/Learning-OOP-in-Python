"""Module For Accounts"""

class Accounts:
    """A class to reprsent Accounts"""

    def __init__(self, name, password, balance):
        """Initialize attributes for single account"""
        self.name = name
        self.password = password
        self.balance = balance

    def withdraw(self, password, balance):
        """Method for withdrawing balance"""
        if password.lower() == self.password:
            if self.balance >= balance:
                self.balance -= balance
            else:
                print("Your do not have enough balance")
                return
        else:
            print("Incorrect password")
            return
    
    def deposit(self, balance, password):
        """Method for depositing balance"""
        if self.password == password.lower():
            if balance > 0:
                self.balance += balance
            else:
                print("You cannot deposit negative amount")
                return
        else:
            print("Incorrect Password")
            return
    
    def check(self):
        """display user information"""
        print(f"Username: {self.name}")
        print(f"Password: {self.password}")
        print(f"Balance: {self.balance}")