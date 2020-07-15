class Action:
    def __init__(self, who, when, action):
        self.who = who
        self.when = when
        self.action = action

    def __repr__(self):
        return self.__dict__.__repr__()