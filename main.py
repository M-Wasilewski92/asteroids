import pygame
from asteroid import Asteroid
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
from circleshape import CircleShape
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    frames_per_second = pygame.time.Clock()
    dt = 0
    updatable  = pygame.sprite.Group()
    drawable  = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    player= Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroids_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for updatable_obj in updatable:
            updatable_obj.update(dt)

        for asteroid in asteroids:
            collision = asteroid.collision(player)
            for shot in shots:
                hit = asteroid.collision(shot)
                if hit:
                    asteroid.split()
                    shot.kill()
            if collision:
                print("Game over!")
                return



        screen.fill("black")
        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        pygame.display.flip()
        dt = frames_per_second.tick(60) / 1000



if __name__ == "__main__":
    main()