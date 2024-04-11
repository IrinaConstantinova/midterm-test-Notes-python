from controller import NoteController
from note_manager import NoteManager
from note_repository import NoteRepository
from view import ConsoleView

if __name__ == "__main__":
    print("\n ---Вас приветствует приложение для заметок!---")
    note_repository = NoteRepository("notes_folder", "notes.json")
    note_manager = NoteManager()
    note_manager.notes = note_repository.load_notes()
    console_view = ConsoleView()
    note_controller = NoteController(note_manager, note_repository, console_view)
    note_controller.run_program()