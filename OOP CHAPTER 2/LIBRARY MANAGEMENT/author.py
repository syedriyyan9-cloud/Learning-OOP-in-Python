"""
A module for defining author
"""

class Author:
    """An author would have name, age, email and the books he has written"""

    def __init__(self, name: str, age: int, email: str) -> None:
        """Creates an author object"""
        self.name = name
        self.age = age
        self.email = email
        self.id = 1

# if __name__ == "__main__":
#     author = Author('riyyan', 22, "asdf@gmail.com",["works","ships"])
#     print(author.name,author.age,author.email,author.books)