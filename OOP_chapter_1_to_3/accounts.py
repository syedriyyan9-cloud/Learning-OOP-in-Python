"""Module For Accounts"""

class AbortTransaction(Exception):
    """A custom exception class"""
    pass

class Accounts:
    """A class to reprsent Accounts"""

    def __init__(self, name: str, password: int, balance: int):
        """Initialize attributes for single account"""

        try:
            self.name = str(name)
            self.password = int(password)
            self.balance = int(balance)
        except ValueError:
            raise AbortTransaction("One of the values are incorrect")

        self.check_amount(self.balance)

    def validate_input(self, password: int, amount: int):
        """Validates the user's password and amount"""

        try:
            amount = int(amount)
            password = int(password)
        except (ValueError, TypeError):
            raise AbortTransaction("Password and Amount should integers")
        
        if password != self.password:
            raise AbortTransaction("Incorrect password")
        
        return password, amount
        
    def check_amount(self, amount: int):
        """Check for negative values and 0 in amount"""

        if amount <= 0:
            raise AbortTransaction("You cannot enter 0 or negative value")

    def withdraw(self, password: int, amount: int):
        """Method for withdrawing balance"""

        password, amount = self.validate_input(password, amount)
        self.check_amount(amount)
        
        if amount > self.balance:
            raise AbortTransaction("Your do not have enough balance")
        
        self.balance -= amount
        
    def deposit(self, amount: int, password: int):
        """Method for depositing balance"""

        password, amount = self.validate_input(password, amount)
        self.check_amount(amount)

        self.balance += amount
        
    
    def check(self):
        """display user information"""

        print(f"Username: {self.name}")
        print(f"Password: {self.password}")
        print(f"Balance: {self.balance}")