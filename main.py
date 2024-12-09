
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
pygame.display.set_caption('Asteroids by Zoolndr')
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

    font = pygame.font.SysFont(None, 36)
    elapsed_frames = 0
    score_counter = [0]
  
    

    while running:
        dt = clock.tick(FPS) / 1000
        
        elapsed_frames += 1
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
                    asteroid.split(score_counter)
                    print("Current score_counter:", score_counter)
                    shot.kill()

        for element in drawable:
            element.draw(screen)
        
        
        timer = elapsed_frames // 60
        minutes = timer // 60
        seconds = timer % 60
        score_count = score_counter[0]    
        
        timer_surface = font.render(f"Time - {minutes}:{seconds:02}", False, (255,255,255))
        timer_rect = timer_surface.get_rect(center=(SCREEN_WIDTH / 2, timer_surface.get_height() / 2))
        score_surface = font.render(f"Score - {score_count}", False, (255,255,255))
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH / 2, timer_rect.bottom + score_surface.get_height() / 2))

        screen.blit(timer_surface, timer_rect.topleft)
        screen.blit(score_surface, score_rect.topleft)

        pygame.display.flip()
    


if __name__ == "__main__":
    main()