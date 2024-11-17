import pygame
from utils import Dimensions as D


class Scenery:
    def __init__(self, image_path):
        self._background = pygame.image.load(image_path).convert()
        self._background = pygame.transform.scale(self._background, (D.SCREEN_WIDTH.value, D.SCREEN_HEIGHT.value))
        self._y = 0

    def draw(self, screen):
        screen.blit(self._background, (0, self._y))
        screen.blit(self._background, (0, self._y - D.SCREEN_HEIGHT.value))
