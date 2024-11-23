import pygame
import os
from utils import Dimensions as D


class Scenery:
    def __init__(self, filename):
        current_dir = os.path.dirname(os.path.dirname(__file__))
        assets_dir = os.path.join(current_dir, "assets", "images")
        self._background_path = os.path.join(assets_dir, filename)

        self._background = pygame.image.load(self._background_path).convert()
        self._background = pygame.transform.scale(
            self._background,
            (D.SCREEN_WIDTH.value, D.SCREEN_HEIGHT.value)
        )
        self._y = 0

    def draw(self, screen):
        screen.blit(self._background, (0, 0))
