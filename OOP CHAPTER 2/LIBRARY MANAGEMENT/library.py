"""
This is a module for defining library
"""

from book import Book

from author import Author

from library_visitors_and_staff import Members, Staff

class Library:
    """Library contains several books, a user can borrow a book, and return it, 
    a staff member can add a new book, remove a book"""

    def __init__(self, name: str = "", location: str = "") -> None:
        """Creates a library object"""
        self.list_of_books = []
        self.library_name = name
        self.location = location