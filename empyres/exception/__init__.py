class GameException(Exception):
    def __init__(self, code, message):
        super().__init__()
        self.code = code
        self.message = message

class MapException(GameException):
    def __init__(self, code, message):
        super().__init__(code, message)

class MapOutOfBoundsException(MapException):
    def __init__(self, aPoint):
        super().__init__('MapOOB', 'Point out of bounds: %s' % (str(aPoint)))
        self.aPoint = aPoint
