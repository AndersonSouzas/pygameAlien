import pygame
from font import CustomFont


class Score:
    def __init__(self, font_size=20, color=(138, 170, 235)):
        self.score = 0
        self.is_game_over = False
        self._custom_font = CustomFont()
        self.color = color
        self.font_size = font_size

    def add_score(self, points: int):
        if not self.is_game_over:
            self.score += points

    def _render_text_centered(self, screen: pygame.Surface, text: str, y_offset: int) -> None:
        screen_width, screen_height = screen.get_size()
        text_surface = self._custom_font.render_font(
            text=text,
            font_size=self.font_size,
            font_color=self.color,
            position=(0, 0)
        )
        text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + y_offset))
        screen.blit(text_surface, text_rect)

    def render_score(self, screen: pygame.Surface) -> None:
        score_text_surface = self._custom_font.render_font(
            text=f"Score: {self.score}",
            font_size=self.font_size,
            font_color=self.color,
            position=(10, 10)
        )
        screen.blit(score_text_surface, (10, 10))

    def render_game_over(self, screen: pygame.Surface) -> None:
        if self.is_game_over:
            self._render_text_centered(screen, "Game Over", -40)
            self._render_text_centered(screen, f"Final Score: {self.score}", 20)

    def trigger_game_over(self):
        self.is_game_over = True
