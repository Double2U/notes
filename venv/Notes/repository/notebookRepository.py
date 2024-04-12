from repository.note import Note
import json
from operator import attrgetter

class NotesRepository:
    
    list_note = []

    def __init__(self):
        self.list_note = self.list_note


    def add(self, note: Note):
        self.readAll()
        self.list_note.append(note)
        note.id_note += len(self.list_note)
        self.save()
            

    def readAll(self):
        self.list_note.clear()
        while(True):
            try:
                with open("notes.json", 'r') as f:
                    notes = json.load(f)
                    for note in notes:
                        n = Note(note["title_note"], note["body_note"])
                        n.id_note = note["id_note"]
                        n.date_create_note = note["date_create_note"]
                        n.date_update_note = note["date_update_note"]
                        self.list_note.append(n)
                    sorted_list = sorted(self.list_note, key= attrgetter("date_update_note"), reverse= True)
                    return sorted_list  
            except FileNotFoundError:
                f = open("notes.json", 'w')
                f.write("[]")
                f.close()   

    
    def read(self, id : int):
        self.readAll()
        if (len(self.list_note) < id or id <= 0):
            print(f"id - {id} not found. Enter right id from list of notes:\n{self.list_note}")
        else:
            return self.list_note[id - 1]   
            
    def save(self):
        with open('notes.json', 'w') as json_file:
            json.dump([n.__dict__ for n in self.list_note], json_file, indent= 4)
        self.list_note.clear()    



    def delete(self, id : int):
        self.readAll()           
        delete_note = self.list_note[id - 1]
        self.list_note.remove(delete_note)
        for i in range(0, len(self.list_note)):
            self.list_note[i].id_note = i + 1   
        self.save() 

    def update(self, id : int, title : str, body : str):
        self.readAll()
        self.list_note[id - 1].title_note = title
        self.list_note[id - 1].body_note = body
        self.list_note[id - 1].date_update_note = Note.date
        self.save()
   

            

