from Comet import Comet
import schema
import board
import neopixel
import random
import time


class Space:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.Objects = []
        self.pixels = neopixel.NeoPixel(board.D0, max_x*max_y)
    def start(self):
        while True:
            wait = random.randint(3, 60)
            elapsed = 0
            
            while elapsed < wait:
                wait -= 1
                elapsed += 1
                for object in self.Objects:
                    for pixel in object.particles:
                        
                time.sleep(0.25)
