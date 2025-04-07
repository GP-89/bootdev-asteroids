import sys

import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    time = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable)

    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                sys.exit("Game Over!")



        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        dt = time.tick(60) / 1000.0

if __name__ == "__main__":
    main()