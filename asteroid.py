from circleshape import CircleShape
from constants import *

import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, 'White', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)


    def split(self, score_counter):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            score_counter[0] += 50
            return
        else:
            angle = random.uniform(20, 50)
            new_ast_1 = self.velocity.rotate(angle)
            new_ast_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            split1 = Asteroid(self.position.x, self.position.y, new_radius)
            split1.velocity = new_ast_1 * 1.2
            split2 = Asteroid(self.position.x, self.position.y, new_radius)
            split2.velocity = new_ast_2 * 1.2


