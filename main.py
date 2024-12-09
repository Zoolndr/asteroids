
######### IMPORTS #########
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
###########################

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True
FPS = 60

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Shot.containers = (shots, updatable, drawable)
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)


def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()


    while running:
        dt = clock.tick(FPS) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill('Black')
        for element in updatable:
            element.update(dt)
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print('Game over')
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                distance = asteroid.position.distance_to(shot.position)
                total_radius = asteroid.radius + shot.radius
                if distance <= total_radius:
                    asteroid.split()
                    shot.kill()

        for element in drawable:
            element.draw(screen)
        pygame.display.flip()
    


if __name__ == "__main__":
    main()