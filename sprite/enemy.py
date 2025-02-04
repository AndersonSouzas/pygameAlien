import pygame
import random
import os
from utils import Dimensions as D


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, speed_x: float, speed_y: float, sprite_path: str):
        super().__init__()
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                            (int(self.image.get_width() * 0.75),
                                             int(self.image.get_height() * 0.75)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed_x = speed_x
        self.speed_y = speed_y
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
    def __init__(self, enemy_group, spawn_interval=8000):
        self.spawn_interval = spawn_interval
        self.enemy_group = enemy_group
        self.last_spawn_time = pygame.time.get_ticks()
        self.screen_width = D.SCREEN_WIDTH.value
        self.screen_height = D.SCREEN_HEIGHT.value
        self.speed_modifier = 1.0
        self.speed_increment_rate = 0.1

        self.enemy_sprites = [
            os.path.join("assets", "images", "sprites", "enemies", "ghost.png"),
            os.path.join("assets", "images", "sprites", "enemies", "spinner.png"),
        ]

    def _generate_random_enemy(self):
        x = random.randint(50, self.screen_width - 50)
        y = random.randint(50, self.screen_height - 50)
        speed_x = random.uniform(2, 4) * random.choice([-1, 1]) * self.speed_modifier
        speed_y = random.uniform(2, 4) * random.choice([-1, 1]) * self.speed_modifier

        sprite_path = random.choice(self.enemy_sprites)

        return Enemy(x, y, speed_x, speed_y, sprite_path)
        
    def initial_spawn(self, count=2):
        for i in range(count):
            self.enemy_group.add(self._generate_random_enemy())

    def spawn_enemy(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time > self.spawn_interval:
            self.enemy_group.add(self._generate_random_enemy())
            self.last_spawn_time = current_time
            self.speed_modifier += self.speed_increment_rate

    def reset_enemies(self):
        self.enemy_group.empty()
        self.initial_spawn()
