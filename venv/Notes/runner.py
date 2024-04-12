from notebookController import Controller
from repository.notebookRepository import NotesRepository
from notebookPresenter import Presenter

def run():

    repository = NotesRepository()
    controller = Controller(repository)
    presenter = Presenter(controller)
    presenter.start()