from circleshape import CircleShape
from constants import *
import pygame


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_SHOT_RADIUS)
        self.velocity = pygame.Vector2(0,0)
        for group in self.containers:
            group.add(self)

    
    def draw(self, screen):
        pygame.draw.circle(screen, 'White', self.position, PLAYER_SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)