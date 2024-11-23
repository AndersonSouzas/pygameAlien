import pygame
from sys import exit
from utils import Dimensions, PlayerAction, PlayerColor
from state import Scenery, PlayerState
from inputs import Keymap
from sprite import Animation

pygame.init()
screen = pygame.display.set_mode((Dimensions.SCREEN_WIDTH.value, Dimensions.SCREEN_HEIGHT.value))
pygame.display.set_caption('Aliens')

clock = pygame.time.Clock()
FPS = 60
scenery = Scenery('background.jpg')

player = PlayerState()
player_color = PlayerColor.BLUE
player_animation = Animation(player, player_color, speed=2.0, scale=0.9, screen=screen)


def game_loop():
    running = True
    while running:
        delta_time = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    
        player_animation.update(delta_time)

        scenery.draw(screen)
        player_animation.render()

        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    exit()


if __name__ == '__main__':
    game_loop()
