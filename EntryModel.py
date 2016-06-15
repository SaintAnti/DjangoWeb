class EntryModel:
    def __init__(self, author, message):
        """Creates an EntryModel object.
        :param author: string
        :param message: string
        """
        self.author = author
        self.message = message

    def to_string(self):
        """Returns a string representation of EntryModel object."""
        return self.author + ' says ' + self.message
