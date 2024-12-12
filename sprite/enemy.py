import pygame
import random
from utils import Dimensions as D


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, speed: float):
        super(). __init__()
        self.image = pygame.image.load("assets/images/sprites/enemys/fishGreen.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
        self.speed_x = speed
        self.speed_y = random.uniform(-2, 2)

        self.screen_width = D.SCREEN_WIDTH.value
        self.screen_height = D.SCREEN_HEIGHT.value

    def update(self):
        self.rect.x -= self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0:
            self.rect.left = 0
            self.speed_x = -self.speed_x
        elif self.rect.right >= self.screen_width:
            self.rect.right = self.screen_width
            self.speed_x = -self.speed_x

        if self.rect.top <= 0:
            self.rect.top = 0
            self.speed_y = -self.speed_y
        elif self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height
            self.speed_y = -self.speed_y
