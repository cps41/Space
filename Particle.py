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

    def set_location(self, x, y):
        """ Method for setting particle location
            
            Params:
                x(int): x axis location
                y(int): y axis location
            Return:
                None
        """
        self.x = x
        self.y = y

    def increment_location(self, x_offset, y_offset):
        """ Method for incrementing particle location
            
            Params:
                x_offset(int): x axis offset
                y_offset(int): y axis offset
            Return:
                (x(int), y(int)): (x axis location, y axis location)
        """
        self.x += x_offset
        self.y += y_offset
        return (self.x, self.y)

    def get_location(self, x, y):
        """ Method for getting particle location
            
            Params:
                None
            Return:
                (x(int), y(int)): (x axis location, y axis location)
        """
        return (self.x, self.y)

