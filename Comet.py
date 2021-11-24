from Particle import Particle
import schema
import random


def is_between(min, actual, max):
    between = True
    if actual < min:
        between = False
    elif actual > max:
        between = False

    return between
class Comet:
    def __init__(self, max_x=20, max_y=20):
        self._epicenter = None
        self._stage = 0
        self._direction = (0, 0)
        self._radius = random.randint(3, 10)
        self._tail = None
        self.particles = []
        self.max_x = max_x
        self.max_y = max_y
        self.get_starting_point()
        self.set_particles()
        
        
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
            
        # get border starting point
        if edge == schema.Edge.TOP:
            self._epicenter = Particle(random.randint(0, self.max_x), 0)
        elif edge == schema.Edge.BOTTOM:
            self._epicenter = Particle(random.randint(0, self.max_x), self.max_y)
        elif edge == schema.Edge.LEFT:
            self._epicenter = Particle(0, random.randint(0, self.max_y))
        else:
            self._epicenter = Particle(self.max_x, random.randint(0, self.max_y))
        
        # get tail coordinates
        self._tail = [(self._radius-(self._direction[0]*r), self._radius-(self._direction[1]*r)) for r in range(self._radius)]
    
    
    def set_particles(self):
        """ Method for setting the location/display of the particles that make up the comet.
            
            Params:
                None
            Returns:
                None
        """
        diameter = (self._radius * 2) + 1

        if self._stage == 0:
            offset_x = -self._radius
            offset_y = -self._radius
            for row in range(diameter):
                offset_x += 1
                self.particles.append([])
                for col in range(diameter):
                    offset_y += 1
                    if row == diameter//2 and col == diameter//2:
                        self.particles[row].append(self._epicenter)
                    else:
                        self.particles[row].append(Particle(self._epicenter.x + offset_x, self._epicenter.y + offset_y))
        
        else:
            for row in range(diameter):
                for col in range(diameter):
                    self.particles[row][col].increment_location(self._direction[0], self._direction[1])
                    if self.particles[row][col] is self._epicenter:
                        # make center bright and lit always
                        self._epicenter.set_present(True, 10)
                    elif (row, col) in self._tail:
                        # make tail lit but randomize brightness
                        self.particles[row][col].set_present(True, random.randint(1, 10))
                    elif is_between(self._radius-2, row, self._radius+2) and is_between(self._radius-2, col, self._radius+2):
                        self.particles[row][col].display()
        
        self._stage += 1


    def debug_string(self):
        build_string = " "
        diameter = self._radius*2+1
        for i in range(diameter):
            build_string += f'{i} '
        for row in range(diameter):
            build_string += f'\n{row} '
            for col in range(diameter):
                if self.particles[row][col].get_present():
                    build_string += 'X '
                else:
                    build_string += '* '
        print(build_string)
        