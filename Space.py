from Comet import Comet
import schema


class Space:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.Objects = []