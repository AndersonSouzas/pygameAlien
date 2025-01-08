from abc import ABC
from .screen import Screen
from pygame import Surface, QUIT, KEYDOWN, K_ESCAPE, K_RETURN, Rect, draw
from font import CustomFont
from os import path
from typing import List
import pygame
from pygame.event import Event
from utils import Dimensions


class MainMenuScreen(Screen, ABC):
    def __init__(self, screen: Surface, on_start, on_quit):
        super().__init__(screen)
        self.title_y = 0
        self.custom_font: CustomFont = CustomFont()
        self.background_image: Surface = self._load_image('background')
        self.on_start = on_start
        self.on_quit = on_quit
        self.buttons = [
            {"text": "Start", "action": self.on_start, "rect": pygame.Rect(300, 200, 200, 50)},
            {"text": "Quit", "action": self.on_quit, "rect": pygame.Rect(300, 300, 200, 50)},
        ]
        self.current_button: int = 0
        self.button_color = (138, 170, 235)
        self.text_color = (255, 255, 255)
        self.rectangle_width = Dimensions.SCREEN_WIDTH.value - 400
        self.rectangle_height = 60
        self.spacing = 20
        self.border_thickness = 5

    def handle_events(self, events: List[Event]):
        for event in events:
            if event.type == QUIT:
                self.on_quit()

            elif event.type == KEYDOWN:
                if self.buttons:
                    if event.key == pygame.K_DOWN and self.buttons:
                        self.current_button = (self.current_button + 1) % len(self.buttons)
                    elif event.key == pygame.K_UP and self.buttons:
                        self.current_button = (self.current_button - 1) % len(self.buttons)
                    elif event.key == K_RETURN:
                        current_button = self.buttons[self.current_button]
                        if 'action' in current_button and callable(current_button['action']):
                            current_button['action']()
                elif event.key == K_ESCAPE:
                    self.on_quit()

    def render(self):
        white_color: tuple[int, int, int] = (255, 255, 255)
        self.screen.fill(white_color)
        self.screen.blit(self.background_image, (0, 0))

        center_position_x = Dimensions.SCREEN_WIDTH.value // 2

        total_height = len(self.buttons) * self.rectangle_height + (len(self.buttons) - 1) * self.spacing
        start_y = (Dimensions.SCREEN_HEIGHT.value - total_height) // 2
        
        title_y = start_y - 60
        self.draw_game_title(center_position_x, title_y)

        for index, button in enumerate(self.buttons):
            button_y = start_y + index * (self.rectangle_height + self.spacing)
            self.draw_button(button["text"], center_position_x, button_y, index == self.current_button)

    def draw_game_title(self, center_x: int, title_y: int):
        game_title: str = "pygameAlien"
        font_size: int = 48
        title_surface: Surface = self.custom_font.render_font(game_title, font_size, self.text_color, (0, 0))
        title_rect = title_surface.get_rect(center=(center_x, title_y))

        self.screen.blit(title_surface, title_rect)

    def draw_button(self, text: str, center_x: int, center_y: int, is_selected: bool):
        black_color: tuple[int, int, int] = (0, 0, 0)
        red_color: tuple[int, int, int] = (255, 0, 0)

        text_surface = self.custom_font.render_font(text, 14, self.text_color, (0, 0))
        text_rect = text_surface.get_rect(center=(center_x, center_y))

        rect_x = center_x - (self.rectangle_width // 2)
        rect_y = center_y - (self.rectangle_height // 2)
        rect = Rect(rect_x, rect_y, self.rectangle_width, self.rectangle_height)

        color = red_color if is_selected else self.button_color
        draw.rect(self.screen, black_color, rect)
        draw.rect(self.screen, color, rect, self.border_thickness)
        self.screen.blit(text_surface, text_rect)

    @staticmethod
    def _load_image(image_name: str) -> Surface:
        try:
            base_path: str = path.dirname(path.dirname(__file__))
            image_path: str = f'assets/images/{image_name}.jpg'
            image_path = path.join(base_path, image_path)
            image: Surface = pygame.image.load(image_path)
            return image
        except pygame.error as e:
            print(f"Erro ao carregar a imagem {image_name}: {e}")
            return pygame.Surface((1280, 720))

    def update(self) -> None:
        pass
