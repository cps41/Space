import enum
import random

class Direction(enum.Enum):
    def __init__(self):
        self.N = 0
        self.S = 1
        self.E = 2
        self.W = 3
        self.NE = 4
        self.NW = 5
        self.SE = 6
        self.SW = 7
        
        
    def get_rand_direction(self):
        direction = random.randint(0, 7)
        if direction == 0:
            return (0, -1)
        elif direction == 1:
            return (0, 1)
        elif direction == 2:
            return self.E
        elif direction == 3:
            return self.W
        elif direction == 4:
            return self.NE
        elif direction == 5:
            return self.NW
        elif direction == 6:
            return self.SE
        elif direction == 7:
            return self.SW
        
class Edge(enum.Enum):
    def __init__(self):
        self.TOP = 0
        self.BOTTOM = 1
        self.LEFT = 2
        self.RIGHT = 3
        
        
    def get_rand_edge(self):
        edge = random.randint(0, 3)
        if edge == 0:
            return self.TOP
        elif edge == 1:
            return self.BOTTOM
        elif edge == 2:
            return self.LEFT
        elif edge == 3:
            return self.RIGHT