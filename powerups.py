import pygame
import random
import math
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from circleshape import CircleShape

class Powerups(CircleShape):
    def __init__(self):
        super().__init__(0, 0, 5)
        self.type = None
        self.active_powerups = []


    def random_chance(self):
        magic_number = random.randrange(0, 2000)
        random_x = random.randrange(0, SCREEN_WIDTH)
        random_y = random.randrange(0, SCREEN_HEIGHT)
        self.powerup_constructor(magic_number, random_x, random_y)
        if self.type == 'Coin':
            self.active_powerups.append((self.type, random_x, random_y))

    def powerup_constructor(self, magic_number, x, y):
        if magic_number <= 2000 and magic_number > 500:
            return
        elif magic_number < 501 and magic_number > 475:
            self.type = 'Nuke'
        elif magic_number < 476 and magic_number > 434:
            self.type = 'Minigun'
        elif magic_number < 435 and magic_number > 380:
            self.type = 'Munitions'
        elif magic_number < 381 and magic_number > 300:
            self.type = 'Ghost'
        elif magic_number < 301 and magic_number > 220:
            self.type = 'Stopwatch'
        elif magic_number < 221 and magic_number > 150:
            self.type = 'Hourglass'
        else:
            self.type = 'Coin'

    
    def powerup_manager(self):

        if len(self.active_powerups) == 3:
            return
        else:
            self.random_chance()

    def render(self, screen):
        for powerup in self.active_powerups:
            powerup_type, x, y = powerup  # Unpack the tuple into its components
            pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)

