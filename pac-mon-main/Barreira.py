from tupy import *

class Barreira(Image):
    def __init__(self, x, y):
        self.file = "pedra.png"
        self.x = x
        self.y = y
        self._hide()   