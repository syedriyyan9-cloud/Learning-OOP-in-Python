"""
A module for defining a general class for members and staff
Members can only borrow or return books
Staff member can borrow, return, add or remove books from library
"""

class Members:
    """A class to define members of a library"""

    def __init__(self, id: int, name: str, age: int, email: str, phone: int) -> None:
        """Creates a member object"""
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone

    def borrow_book(self):
        """Allows members to borrow a book"""
        pass

    def return_book(self):
        """Members can return book"""
        pass

class Staff(Members):
    """A class to define staff for library, they can perform all the methods of a member
    they can also perform additional opertions in a library"""

    def __init__(self, id: int, name: str, age: int, email: str, phone: int) -> None:
        """Creates staff members"""
        super().__init__(id, name, age, email, phone)

    def add_book(self):
        """Adds a book to library"""
        pass

    def remove_book(self):
        """Removes a book from library"""
        pass

# if __name__ == "__main__":
#     staff = Staff(1,"riyyan",22,"w@age.com",12312)
#     print(staff.name, staff.age)