from typing import Protocol
from repository.note import Note

class Repository(Protocol):


    def add(self, note : Note):
        pass

    def save(self):
        pass

    def delete(self, id : int):
        pass

    def update(self, id: int, title : str, body : str):
        pass

    def readAll(self) -> list:
        pass

    def read(self, id: int):
        pass