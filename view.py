

class ConsoleView:

    @staticmethod
    def input_command(number_of_command):
        while number_of_command < 1 or number_of_command > 5:
            number_of_command = int(input("---Ошибка, не существует комманды с таким номером!---\n"))
        return number_of_command

    @staticmethod
    def input_note_data():
        title = input("Введите заголовок заметки: ")
        body = input("Введите заметку: ")
        return title, body

    @staticmethod
    def display_notes(notes):
        if notes:
            for note in notes:
                print(f"Номер заметки: {note.note_id}, Заголовок: {note.title}, Заметка: {note.body},"
                      f" Дата создания: {note.created_at}, Последние изменения: {note.update_at}")
        else:
            print("---Заметок нет---")

    @staticmethod
    def display_message(message):
        print(message)


