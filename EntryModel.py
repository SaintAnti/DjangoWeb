class EntryModel:
    def __init__(self, author, message ):
        self.author = author
        self.message = message

    def to_string(self):
        return self.author + ' says ' + self.message
