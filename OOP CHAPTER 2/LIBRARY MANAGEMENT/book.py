"""
This is module for defining book class
"""
class Book:
    """Book object with isbn, genre, page and content attributes"""

    def __init__(self, isbn:int = 0, genre:str = "", pages:int = 0, title:str = "") -> None:
        """Creates a book object"""
        self.isbn = isbn
        self.genre = genre
        self.page = pages
        self.title = title
