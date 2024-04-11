from _datetime import datetime


class Note:

    def __init__(self, note_id, title, body, created_at=None, update_at=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at or datetime.now()
        self.update_at = update_at or datetime.now()

    def update(self, title, body):
        self.title = title
        self.body = body
        self.update_at = datetime.now()
