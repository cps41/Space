import enum
import random

class Direction(enum.Enum):
    N = 0
    S = 1
    E = 2
    W = 3
    NE = 4
    NW = 5
    SE = 6
    SW = 7
        
    def get_rand_direction():
        direction = random.randint(0, 7)
        if direction == Direction.N.value:
            return (0, -1)
        elif direction == Direction.S.value:
            return (0, 1)
        elif direction == Direction.E.value:
            return (1, 0)
        elif direction == Direction.W.value:
            return (-1, 0)
        elif direction == Direction.NE.value:
            return (1, -1)
        elif direction == Direction.NW.value:
            return (-1, -1)
        elif direction == Direction.SE.value:
            return (1, 1)
        elif direction == Direction.SW.value:
            return (-1, 1)
        
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