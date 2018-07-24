

class ExcessPlayerException(Exception):
    def __init__(self):
        message = "Only 2 players can play this game."
        super(ExcessPlayerException, self).__init__(message)