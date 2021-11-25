import enum
import random

class Direction(enum.Enum):
    N = (0, -1)
    S = (0, 1)
    E = (1, 0)
    W = (-1, 0)
    NE = (1, -1)
    NW = (-1, -1)
    SE = (1, 1)
    SW = (-1, 1)
        
    def get_rand_direction():
        return random.choice(list(Direction.__members__.values())).value

        
class Edge(enum.Enum):
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3
        
        
    def get_rand_edge():
        edge = random.randint(0, 3)
        if edge == 0:
            return Edge.TOP
        elif edge == 1:
            return Edge.BOTTOM
        elif edge == 2:
            return Edge.LEFT
        elif edge == 3:
            return Edge.RIGHT