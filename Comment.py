class Comment:
    def __init__(self, who, when, text):
        self.who = who
        self.when = when
        self.text = text

    def __repr__(self):
        return self.__dict__.__repr__()
