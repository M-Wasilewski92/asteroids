import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 1 )

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt

    def collision(self, other):
        return self.position.distance_to(other.position) < self.radius + other.radius

    def split(self):
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        vector_one =self.velocity.rotate(angle)
        vector_two = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        obj_one = Asteroid(self.position.x, self.position.y, new_radius)
        obj_one.velocity = vector_one * 1.2
        obj_two = Asteroid(self.position.x, self.position.y, new_radius)
        obj_two.velocity = vector_two * 1.2
        self.kill()