

class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.note_id != note_id]

    def edit_note(self, note_id, new_title, new_body):
        for note in self.notes:
            if note_id == note_id:
                note.update(new_title, new_body)
                break

    def get_notes(self, filter_date=None):
        if filter_date:
            return [note for note in self.notes if note.update_at.date() == filter_date.date()]
        else:
            return self.notes

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note_id == note.note_id:
                return note
        return None