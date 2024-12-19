import pygame
from state import PlayerState


class CollisionManager:
    def __init__(self, player_state: PlayerState, enemy_group: pygame.sprite.Group):
        self.player_state = player_state
        self.enemy_group = enemy_group

    def check_collisions(self) -> bool:
        return any(self.player_state.rect.colliderect(enemy.rect) for enemy in self.enemy_group)
