from enum import Enum

class Commands(Enum):
    ADD = ("ADD", "create and add note")
    READ = ("READ","read note")
    UPDATE = ("UPDATE", "update note")
    READALL =("READALL", "read list note")
    DELETE = ("DELETE","delete note")
    HELP = ("HELP", "print list of command")
    EXIT = ("EXIT", "exit from programm")
