import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = updatable, drawable
Asteroid.containers = updatable, drawable, asteroids
AsteroidField.containers = updatable
Shot.containers = updatable, drawable, shots

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)

        for entity in updatable:
            entity.update(dt)

        for entity in asteroids:
            if player.collision(entity):
                print("Game Over!")
                pygame.QUIT
                return
            for bullet in shots:
                if bullet.collision(entity):
                    entity.split()
                    bullet.kill()
        
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time()/1000
    

if __name__ == "__main__":
    main()