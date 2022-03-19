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
    
    def get_description(x, y):
        if x == 0:
            if y == -1: return "N"
            else: return "S"
        elif x == 1:
            if y == 0: return "E"
            elif y == 1: return "SE"
            else: return "NE"
        else:
            if y == 0: return "W"
            elif y == 1: return "SW"
            else: return "NW"

        
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


class Color(enum.Enum):
    WHITE = (230, 230, 230)
    MAX_WHITE = (255, 255, 255)
    BLACK = (0,0,0)