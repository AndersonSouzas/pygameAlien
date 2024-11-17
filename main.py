import pygame
import os
from sys import exit
from utils import Dimensions
from state import Scenery

pygame.init()
screen = pygame.display.set_mode((Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value))
pygame.display.set_caption('Aliens')

clock = pygame.time.Clock()
FPS = 60
base_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir, 'assets', 'images', 'background.jpg')
background = Scenery(image_path)


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

        background.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_loop()
