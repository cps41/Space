from Particle import Particle
import schema

import random

class Comet:
    def __init__(self, max_x, max_y):
        self._epicenter = None
        self._stage = 0
        self._direction = (0, 0)
        self._radius = random.randint(2, 5)
        self.particles = []
        self.max_x = max_x
        self.max_y = max_y
        
        
    def get_starting_point(self):
        """ Method for initializing comet's direction and starting point. The comet can start from anywhere so long as it's a point 
            on the border of the given grid. 
            
            Params:
                None
            Returns:
                None
        """
        self._direction = schema.Direction.get_rand_direction()
        edge = schema.Edge.get_rand_edge()
            
        if edge == schema.Edge.TOP:
            self._epicenter = Particle(random.randint(0, self.max_x), 0)
        elif edge == schema.Edge.BOTTOM:
            self._epicenter = Particle(random.randint(0, self.max_x), self.max_y)
        elif edge == schema.Edge.LEFT:
            self._epicenter = Particle(0, random.randint(0, self.max_y))
        else:
            self._epicenter = Particle(self.max_x, random.randint(0, self.max_y))
    
    
    def set_particles(self):
        """ Method for setting the location/display of the particles that make up the comet.
            
            Params:
                None
            Returns:
                None
        """
        if self._stage == 0:
            self.particles = [self._epicenter]
            offset_x = -self._radius
            offset_y = -self._radius
            for row in range(self._radius*2):
                offset_x += 1
                self.particles.append([])
                for col in range(self._radius*2):
                    offset_y += 1
                    self.particles[row].append(Particle(self._epicenter.x + offset_x, self._epicenter.y + offset_y))
        
        else:
            for row in range(self._radius*2):
                for col in range(self._radius*2):
                    self.particles[row][col].increment_location(self._direction[0], self._direction[1])
                    self.particles[row][col].display()
        
        self._stage += 1


    def debug_string(self):
        build_string = ""
        for row in range(self._radius*2):
            build_string += '\n'
            for col in range(self._radius*2):
                if self.particles[row][col].get_present():
                    build_string += 'X'
                else:
                    build_string += 'O'
        