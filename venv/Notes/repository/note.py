import time
from typing import Any

class Note():
    
    id_note = 0
    date = time.strftime("%d %b %Y %H %M %S", time.localtime())

    def __init__(self, title_note, body_note):
        self.id_note = self.id_note
        self.title_note = title_note
        self.body_note = body_note
        self.date_create_note = time.strftime("%d %b %Y %H %M %S", time.localtime())
        self.date_update_note = self.date_create_note

    def get_id_note(self) -> int:
        return self.id_note
    
    def get_title_note(self) -> str:
        return self.title_note
    
    def set_title_note(self, title):
        self.title_note = title
    
    def get_body_note(self) -> str:
        return self.body_note
    
    def set_body_note(self, body):
        self.body_note = body

    def get_date_create_note(self) -> str:
        return self.date_create_note  
    
    def get_date_update_note(self) -> str:
        return self.date_update_note
    

    def __repr__(self) -> str:
        return f"\nid: {self.id_note}\ncreate_date: {self.date_create_note}\ntitle: {self.title_note}\nbody: {self.body_note}\nupdate_date: {self.date_update_note}\n"
    