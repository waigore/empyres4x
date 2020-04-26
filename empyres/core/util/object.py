from .registry import register

class GameObject(object):
    def __init__(self, type):
        self.type = type
        self.uuid = register(self)
