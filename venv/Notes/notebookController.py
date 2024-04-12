from repository.repository import Repository
from repository.note import Note


class Controller:

    def __init__(self, repository: Repository ):
        self.repository = repository

    def add_note(self, note: Note):
        self.repository.add(note)

    def read_notes(self) -> list:
        return self.repository.readAll()

    def read_by_id(self, id: int):
        return self.repository.read(id)    

    def delete_note(self, id : int):
        self.repository.delete(id)
        
    def update_note(self, id: int, title, body):
        self.repository.update(id, title, body)

