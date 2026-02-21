"""
A python module that would be used to create note objects
"""

from datetime import datetime

class Note:
    """A class to represent notes"""
    id = 0
    def __init__(self):
        """Initialize attributes"""
        self.content = ""
        self.time = datetime.now()
        self.tag = ""
        self.writer = ""
        Note.id += 1