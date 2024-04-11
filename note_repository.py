import json
import os

from note import Note


class NoteRepository:
    def __init__(self, directory_name, file_name):
        self.directory_name = directory_name
        self.file_name = os.path.join(directory_name, file_name)
        self.create_directory()

    def create_directory(self):
        if not os.path.exists(self.directory_name):
            os.makedirs(self.directory_name)

    def save_notes(self, notes):
        with open(self.file_name, 'w') as file:
            json.dump([note.__dict__ for note in notes], file, default=str)

    def load_notes(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
                return [Note(**note_data) for note_data in data]
        except FileNotFoundError:
            return []