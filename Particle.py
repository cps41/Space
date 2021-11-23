import random


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.present = False
        self.brightness = 0
    
    
    def display(self):
        """ Method for randomly setting particle to display
            
            Params:
                None
            Returns:
                display(Boolean): True for display on, False for display off
        """
        return bool(random.getrandbits(1))
    
    def set_present(self, present):
        """ Method for forcibly setting particle to display
            
            Params:
                present(Boolean): True for display on, False for display off
            Returns:
                None
        """
        self.present = present
        
    def get_present(self):
        """ Method for getting particle display status
            
            Params:
                None
            Return:
                display(Boolean): True for display on, False for display off
        """
        return self.present
