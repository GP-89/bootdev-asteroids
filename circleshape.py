import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, object):
        distance = pygame.Vector2(object.position - self.position)
        if distance.length() < self.radius:
            return True
        else:
            return False