import note_manager
from note import Note


class NoteController:

    def __init__(self, note_manager, note_repository, console_view):
        self.note_manager = note_manager
        self.note_repository = note_repository
        self.console_view = console_view

    def commands(self, command):
        command = self.console_view.input_command(command)
        while command != 5:
            command = int(input("Выберите команду:\n"
                                "1. Добавить заметку\n"
                                "2. Удалить заметку\n"
                                "3. Редактировать заметку\n"
                                "4. Вывести список всех заметок\n"
                                "5. Выход\n"
                                "Введите номер команды: "))

            if command == 1:
                title, body = self.console_view.input_note_data()
                note_id = len(self.note_manager.notes) + 1
                note = Note(note_id, title, body)
                self.note_manager.add_note(note)
                self.note_repository.save_notes(self.note_manager.notes)
                self.console_view.display_message("---Заметка успешно добавлена!---")
            elif command == 2:
                note_id = int(input("Введите номер заметки для удаления: "))
                if self.note_manager.get_note_by_id(note_id):
                    self.note_manager.delete_note(note_id)
                    self.note_repository.save_notes(self.note_manager.notes)
                    self.console_view.display_message("---Заметка успешно удалена!---")
                else:
                    self.console_view.display_message("---Заметка с указанным номером не существует!---")
            elif command == 3:
                note_id = int(input("Введите номер заметки для редактирования: "))
                if self.note_manager.get_note_by_id(note_id):
                    title, body = self.console_view.input_note_data()
                    self.note_manager.edit_note(note_id, title, body)
                    self.note_repository.save_notes(self.note_manager.notes)
                    self.console_view.display_message("---Заметка успешно отредактирована!---")
                else:
                    self.console_view.display_message("---Заметка с указанным номером не существует!---")
            elif command == 4:
                notes = self.note_manager.get_notes()
                self.console_view.display_notes(notes)
            elif command == 5:
                return
            else:
                self.console_view.display_message("---Ошибка, не существует комманды с таким номером!---")

    def run_program(self):
        command = self.console_view.input_command(1)
        self.commands(command)
