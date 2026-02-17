"""
A module that defines note book class
"""

from note import Note

class NoteBook:
    """A class to represent note book"""

    def __init__(self):
        """Initialize notebook's attributes"""
        self.list_of_notes = {}
        self.id = 1

    def add(self):
        """Add new notes to notebook"""
        note = Note()
        content = input("Add content: ")
        note.content = content
        tag = input("Add tag: ")
        note.tag = tag
        writter = input("Name of the writter: ")
        note.writter = writter
        self.list_of_notes[self.id] = note
        self.id += 1

    def search(self):
        """Search for notes using tags"""
        tag = input("Enter Tag name to search: ")
        for key, value in self.list_of_notes.items():
            if value.tag == tag:
                print("Here is the following note: ")
                print("Time: ", value.time)
                print("Writter: ", value.writter)
                print("Content: ", value.content)
                return key, value
        print("No Tag name found")

    def modify(self):
        """Modify existing notes"""
        key, value = self.search()
        change = input("now you can add more info to it: ")
        value.content += change
        self.list_of_notes[key] = value
        print("Successfully added new data")

    def delete(self):
        """Delete notes from notebook"""
        key, value = self.search()
        print(f"This note was written by: {value.writter} at {value.time}")
        delete = input("Write 'delete this note' to delete the note: ")
        if delete == 'delete this note':
            del self.list_of_notes[key]
            print("Successfully deleted")
