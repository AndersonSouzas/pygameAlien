import pygame
from sys import exit
from utils import Dimensions, PlayerColor, Score
from state import Scenery, PlayerState, CollisionManager
from sprite import Animation, EnemyManager

pygame.init()
screen = pygame.display.set_mode((Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value))
pygame.display.set_caption('Aliens')

clock = pygame.time.Clock()
FPS = 60
scenery = Scenery('background.jpg')

player = PlayerState()
player_color = PlayerColor.YELLOW
player_animation = Animation(player, player_color, speed=800.0, scale=1.0, screen=screen)

enemy_group = pygame.sprite.Group()
enemy_manager = EnemyManager(enemy_group)

collision_manager = CollisionManager(player, enemy_group)
score_system = Score()


def game_loop():
    running = True
    elapsed_time = 0
    enemy_manager.initial_spawn()

    while running:
        delta_time = clock.tick(FPS) / 1000.0
        elapsed_time += delta_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                if event.key == pygame.K_r and score_system.is_game_over:
                    score_system.is_game_over = False
                    score_system.score = 0
                    elapsed_time = 0
                    enemy_manager.reset_enemies()
                    player.reset_position()

        if not score_system.is_game_over:
            if elapsed_time >= 1:
                score_system.add_score(10)
                elapsed_time = 0

            player_animation.update(delta_time)
            enemy_manager.spawn_enemy()
            enemy_group.update()

            sprite_width, sprite_height = player_animation.get_current_sprite_animation()
            player.update_rect(sprite_width, sprite_height)

            if collision_manager.check_collisions():
                score_system.trigger_game_over()

        scenery.draw(screen)
        player_animation.render()
        enemy_group.draw(screen)

        score_system.render_score(screen)

        if score_system.is_game_over:
            score_system.render_game_over(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_loop()
