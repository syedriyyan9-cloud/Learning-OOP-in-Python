"""
A module that defines note book class
"""

from note import Note

class NoteBook:
    """A class to represent note book"""

    def __init__(self):
        """Initialize notebook's attributes"""
        self.list_of_notes = {}
        self.file = "./OOP CHAPTER 2/NOTEBOOK PRACTICE/file.txt"
        self.note = 0

    def add(self: None) -> None:
        """Add new notes to notebook"""
        self.note = Note()
        content = input("Add content: ")
        self.note.content = content
        tag = input("Add tag: ")
        self.note.tag = tag
        writer = input("Name of the writter: ")
        self.note.writer = writer
        self._add_content_to_file(self.note)
        self.list_of_notes[self.note.id] = self.note

    def _add_content_to_file(self, note:Note) -> None:
        """Adds content to the file with ID, owner, tag and content"""
        with open(self.file, 'a') as file:
                file.writelines("\n"+f"ID: {note.id}\nWritten by: {note.writer}\n"
                                f"Tag: {note.tag}\n"
                                f"Content: {note.content}")
                return
        print("The data cannot be written!")

    def search(self: None) -> int:
        """Search for notes using tags"""
        id = int(input("Enter ID to search: "))
        if self.list_of_notes.get(id):
            print("Here is the following note: ")
            print("Time: ", self.list_of_notes[id].time)
            print("Writer: ", self.list_of_notes[id].writer)
            print("Content: ", self.list_of_notes[id].content)
            return id
        print("No ID found")

    def modify(self: None) -> None:
        """Modify existing notes"""
        key = self.search()
        change = input("now you can add more info to it: ")
        self.list_of_notes[key].content += change
        print("Successfully added new data")

    def delete(self: None) -> None:
        """Delete notes from notebook"""
        key = self.search()
        print(f"This note was written by: {self.list_of_notes[key].writer} "
            f"at {self.list_of_notes[key].time}")
        delete = input("Write 'delete this note' to delete the note: ")
        if delete == 'delete this note':
            del self.list_of_notes[key]
            print("Successfully deleted")
