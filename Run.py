import time
from machine import Pin
import neopixel
import random



class Space:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.Objects = []
        self.pixels = neopixel.NeoPixel(Pin(15, Pin.OUT), width*height, brightness=0.5)
    def coordinates_to_index(self, col, row):
        """ Expected input is a pixel's x, y which translates to (col, row) in a grid 
            Formula for converting coordinates of a grid to an index is (width*row)+col """
        return self.width(row) + col
    def create_object(self, obj_type):
        """ Method for randomly generating objects such as comets and stars """
        i = random.randint(0, 100)
        if i%3 == 0:
            if isinstance(obj_type, Comet):
                new_obj = obj_type(max_x=self.width, max_y=self.height)
                self.Objects.append(new_obj)
    def check_in_bounds(self, x, y):
        """ Check if a pixel is within the grid bounds """
        in_bounds = True
        if x < 0 or x >= self.width:
            in_bounds = False
        if y <0 or y >= self.height:
            in_bounds = False
        return in_bounds
    def update_pixels(self):
        """ 'Event loop' for updating pixels """
        for pixel in self.pixels:
            pixel = Color.BLACK
        time.sleep(random.randint(3, 60))
        stale_objects = []
        for object in self.Objects:
            in_bounds = []
            if isinstance(object, Comet):
                for pixel in object.particles:
                    if isinstance(pixel, Particle):
                        valid = self.check_in_bounds(pixel.get_location())
                        in_bounds.append(valid)
                        if valid:
                            i = self.coordinates_to_index(pixel.get_location())
                            self.pixels[i] = Color.WHITE
            if not any(in_bounds):
                stale_objects.append(object)
        for obj in stale_objects:
            self.Objects.remove(obj)
        time.sleep(0.25)
    def start(self):
        print(f"***********Creating space grid of size {self.width} by {self.height}***********")
        print("Starting Events...")
        while True:
            self.create_object(Comet)
            self.update_pixels()
            self.pixels.show()


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
        self._available_x = []
        self._available_y = []
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
        self._direction = Direction.get_rand_direction()
        edge = Edge.get_rand_edge()
            
        # get border starting point
        if edge == Edge.TOP:
            self._epicenter = Particle(random.randint(0, self.max_x), 0)
        elif edge == Edge.BOTTOM:
            self._epicenter = Particle(random.randint(0, self.max_x), self.max_y)
        elif edge == Edge.LEFT:
            self._epicenter = Particle(0, random.randint(0, self.max_y))
        else:
            self._epicenter = Particle(self.max_x, random.randint(0, self.max_y))
        
        # get tail coordinates
        self._tail = [(self._radius-(self._direction[1]*r), self._radius-(self._direction[0]*r)) for r in range(self._radius)]

        # get bulk head
        if self._direction == Direction.N \
            or self._direction == Direction.NE \
            or self._direction == Direction.NW:
            self._available_y = [y for y in range(1, self._radius)]
        elif self._direction == Direction.E \
            or self._direction == Direction.W:
            self._available_y = [y for y in range(self._radius//2, self._radius+self._radius//2)]
        else:
            self._available_y = [y for y in range(self._radius-1, self._radius*2)]
        
        if self._direction == Direction.E \
            or self._direction == Direction.NE \
            or self._direction == Direction.SE:
            self._available_x = [x for x in range(self._radius-1, self._radius*2)]
        elif self._direction == Direction.W \
            or self._direction == Direction.NW \
            or self._direction == Direction.SW:
            self._available_x = [x for x in range(1, self._radius)]
        else:
            self._available_x = [x for x in range(self._radius//2, self._radius+self._radius//2)]
    
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
                    elif col in self._available_x and row in self._available_y:
                        self.particles[row][col].display()
        
        self._stage += 1


    def debug_string(self):
        direction = Direction.get_description(self._direction[0], self._direction[1])
        build_string = f"Direction: {direction}\n  \t"
        diameter = self._radius*2+1
        for i in range(diameter):
            build_string += f'{i} '
        for row in range(diameter):
            build_string += f'\n{row}\t'
            for col in range(diameter):
                if self.particles[row][col].get_present():
                    build_string += 'X '
                else:
                    build_string += '* '
        print(build_string)


def print_debug_string(iter=10, max_x=20, max_y=20):
    comet = Comet(20, 20)
    for i in range(iter):
        comet.set_particles()
        comet.debug_string()
        time.sleep(0.5)
    return comet

class Direction:
    N = (0, -1)
    S = (0, 1)
    E = (1, 0)
    W = (-1, 0)
    NE = (1, -1)
    NW = (-1, -1)
    SE = (1, 1)
    SW = (-1, 1)
        
    def get_rand_direction():
        return random.choice(list(Direction.__members__.values()))
    
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

        
class Edge:
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


class Color:
    WHITE = (230, 230, 230)
    MAX_WHITE = (255, 255, 255)
    BLACK = (0,0,0)
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
        self.present = bool(random.getrandbits(1))
        self.brightness = random.randint(1, 10)
    
    def set_present(self, present, brightness):
        """ Method for forcibly setting particle to display
            
            Params:
                present(Boolean): True for display on, False for display off
            Returns:
                None
        """
        self.present = present
        self.brightness = brightness
        
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

    def get_location(self):
        """ Method for getting particle location
            
            Params:
                None
            Return:
                (x(int), y(int)): (x axis location, y axis location)
        """
        return self.x, self.y


def main():
    space = Space(16, 16)
    space.start()

if __name__ == '__main__':
    main()