import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
from circleshape import CircleShape
from player import Player
def main():
    pygame.init()
    frames_per_second = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen, )
        pygame.display.flip()
        dt = frames_per_second.tick(60) / 1000


if __name__ == "__main__":
    main()