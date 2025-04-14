import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)


    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Step 1: Kill the current asteroid
        self.kill()

        # Step 2: Check if the asteroid is too small to split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Step 3: Generate random angles for the two new directions
        random_angle = random.uniform(20, 50)
        new_velocity_1 = self.velocity.rotate(random_angle)  # First direction
        new_velocity_2 = self.velocity.rotate(-random_angle)  # Opposite direction

        # Step 4: Compute the new, smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Step 5: Create the first new asteroid
        asteroid_1 = Asteroid(
            x=self.position[0],  # X-coordinate
            y=self.position[1],  # Y-coordinate
            radius=new_radius  # Smaller radius
        )
        asteroid_1.velocity = new_velocity_1 * 1.2  # Set its velocity after creation

        # Step 6: Create the second new asteroid
        asteroid_2 = Asteroid(
            x=self.position[0],  # X-coordinate
            y=self.position[1],  # Y-coordinate
            radius=new_radius  # Smaller radius
        )
        asteroid_2.velocity = new_velocity_2 * 1.2