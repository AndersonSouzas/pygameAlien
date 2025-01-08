from .screen import Screen
import pygame
from pygame import Surface, QUIT, KEYDOWN, K_ESCAPE, K_r
from typing import Callable, List
from utils import PlayerColor, Score
from state import Scenery, PlayerState, CollisionManager
from sprite import Animation, EnemyManager
from pygame.event import Event


class GameScreen(Screen):
    def __init__(self, screen: Surface, on_quit: Callable):
        super().__init__(screen)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.running = True

        self.scenery = Scenery('background.jpg')
        self.player = PlayerState()
        self.player_color = PlayerColor.YELLOW
        self.player_animation = Animation(self.player, self.player_color, speed=600.0, scale=1.0, screen=self.screen)

        self.enemy_group = pygame.sprite.Group()
        self.enemy_manager = EnemyManager(self.enemy_group)
        self.collision_manager = CollisionManager(self.player, self.enemy_group)
        self.score_system = Score()

        self.elapsed_time = 0
        self.on_quit = on_quit

    def handle_events(self, events: List[Event]) -> None:
        for event in events:
            if event.type == QUIT:
                self.running = False
                self.on_quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                    self.on_quit()
                if event.key == K_r and self.score_system.is_game_over:
                    self.reset_game()

    def reset_game(self):
        self.score_system.is_game_over = False
        self.score_system.score = 0
        self.elapsed_time = 0
        self.enemy_manager.reset_enemies()
        self.player.reset_position()

    def update(self):
        delta_time = self.clock.tick(self.FPS) / 1000.0

        if not self.score_system.is_game_over:
            self.elapsed_time += delta_time
            if self.elapsed_time >= 1:
                self.score_system.add_score(10)
                self.elapsed_time = 0

            self.player_animation.update(delta_time)
            self.enemy_manager.spawn_enemy()
            self.enemy_group.update()

            sprite_width, sprite_height = self.player_animation.get_current_sprite_animation()
            self.player.update_rect(sprite_width, sprite_height)

            if self.collision_manager.check_collisions():
                self.score_system.trigger_game_over()

    def render(self):
        self.scenery.draw(self.screen)
        self.player_animation.render()
        self.enemy_group.draw(self.screen)

        self.score_system.render_score(self.screen)
        if self.score_system.is_game_over:
            self.score_system.render_game_over(self.screen)

        pygame.display.flip()

    def run(self):
        self.enemy_manager.initial_spawn()

        while self.running:
            events = pygame.event.get()
            self.handle_events(events)

            self.update()
            self.render()

        pygame.quit()
