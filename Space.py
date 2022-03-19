from Comet import Comet
from Particle import Particle
import logging
import schema
import board
import neopixel
import random
import time


LOG = logging.Logger("Space")


class Space:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.Objects = []
        self.pixels = neopixel.NeoPixel(board.D0, width*height, brightness=0.5)
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
            pixel = schema.Color.BLACK
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
                            self.pixels[i] = schema.Color.WHITE
            if not any(in_bounds):
                stale_objects.append(object)
        for obj in stale_objects:
            self.Objects.remove(obj)
        time.sleep(0.25)
    def start(self):
        LOG.info(f"***********Creating space grid of size {self.width} by {self.height}***********")
        LOG.info("Starting Events...")
        while True:
            self.create_object()
            self.update_pixels()
            self.pixels.show()