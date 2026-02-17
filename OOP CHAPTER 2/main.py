"""
the main file for executing notebook program
"""
import sys

from note_book import NoteBook

def display():
    """Shows menu to access notebook"""
    notebook = NoteBook()
    while True:
        print("1: Add a note")
        print("2: Search a note")
        print("3: Modify a note")
        print("4: Delete a note")
        print("5: Exit program")
        user = int(input("Select an option: "))
        match user:
            case 1:
                notebook.add()
            case 2:
                notebook.search()
            case 3:
                notebook.modify()
            case 4:
                notebook.delete()
            case 5:
                sys.exit()
        

if __name__ == "__main__":
    display()

