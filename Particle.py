import random

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.present = False
        self.brightness = 0
    
    
    def display():
        """ Method for randomly setting particle to display
            
            Params:
                None
            Return:
                display(Boolean): True for display on, False for display off
        """
        return bool(random.getrandbits(1))
