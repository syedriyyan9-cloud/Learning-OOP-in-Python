"""
A python module that would be used to create note objects
"""

from datetime import datetime

class Note:
    """A class to represent notes"""

    def __init__(self):
        """Initialize attributes"""
        self.content = ""
        self.time = datetime.now()
        self.tag = ""
        self.writter = ""