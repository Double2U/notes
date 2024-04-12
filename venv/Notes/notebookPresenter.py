from notebookController import Controller
from repository.note import Note
from util.commands import Commands
from repository.repository import Repository



class Presenter:

    
    def __init__(self, controller: Controller):
        self.controller = controller

    def start(self):
        print("Commands:")
        for commands in Commands:
            print(f"{commands.name} - {commands.value[1]}")
        while(True):
            command = input("Enter command: ").upper()
            match (command):
                case "ADD":
                    title = input("Enter title of note: ")
                    body = input ("Enter body of note: ")
                    note = Note(title, body)
                    self.controller.add_note(note)
                    print("Note added")
                case "READ":
                    print(self.controller.read_notes())
                    id = int (input("Enter id of note: "))
                    print(f"\nCurrent note:{self.controller.read_by_id(id)}")
                case "READALL":    
                    print(self.controller.read_notes())
                case "DELETE":
                    print(self.controller.read_notes())
                    id = int (input("Enter id of note: "))
                    self.controller.delete_note(id)
                case "UPDATE":
                    print(self.controller.read_notes())
                    id = int (input("Enter id of note: "))
                    title = input("Enter new title of note: ")
                    body = input ("Enter new body of note: ")
                    self.controller.update_note(id, title, body)
                    print("Note updated")
                case "HELP":
                    print("Commands:")
                    for commands in Commands:
                        print(f"{commands.name} - {commands.value[1]}")    
                case "EXIT":
                    return    
                case _:
                    print("Command not found. Try again.")
                    return    


            
            

            

        
