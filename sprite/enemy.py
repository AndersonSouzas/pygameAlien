import pygame
import random
from utils import Dimensions as D


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, speed: float):
        super().__init__()
        self.image = pygame.image.load("assets/images/sprites/enemys/fishGreen.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed_x = speed
        self.speed_y = speed
        self.screen_width = D.SCREEN_WIDTH.value
        self.screen_height = D.SCREEN_HEIGHT.value

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.speed_x = -self.speed_x
        if self.rect.top < 0 or self.rect.bottom > self.screen_height:
            self.speed_y = -self.speed_y


class EnemyManager:
    def __init__(self, enemy_group, spawn_interval=2000):
        self.spawn_interval = spawn_interval
        self.enemy_group = enemy_group
        self.last_spawn_time = pygame.time.get_ticks()
        self.screen_width = D.SCREEN_WIDTH.value
        self.screen_height = D.SCREEN_HEIGHT.value

    def _generate_random_enemy(self):
        x = random.randint(50, self.screen_width - 50)
        y = random.randint(50, self.screen_height - 50)
        speed = random.randint(2, 6)
        return Enemy(x, y, speed)
        
    def initial_spawn(self, count=3):
        for i in range(count):
            self.enemy_group.add(self._generate_random_enemy())

    def spawn_enemy(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > self.spawn_interval:
            self.enemy_group.add(self._generate_random_enemy())
            self.last_spawn_time = current_time
