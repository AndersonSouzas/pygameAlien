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

    def render_score(self, screen: pygame.Surface) -> None:
        score_text_surface = self._custom_font.render_font(text=f"Score: {self.score}",
                                                           font_size=self.font_size,
                                                           font_color=self.color,
                                                           position=(10, 10))
        screen.blit(score_text_surface, (10, 10))

    def render_game_over(self, screen: pygame.Surface) -> None:

        if self.is_game_over:
            screen_width, screen_height = screen.get_size()

            game_over_text_surface = self._custom_font.render_font(
                text=f"Game Over",
                font_size=self.font_size,
                font_color=self.color,
                position=(screen_width // 2, screen_height // 2 - 40)
            )
            game_over_rect = game_over_text_surface.get_rect(center=(screen_width // 2, screen_height // 2 - 40))

            final_score_text_surface = self._custom_font.render_font(
                text=f"Final Score: {self.score}",
                font_size=self.font_size,
                font_color=self.color,
                position=(screen_width // 2, screen_height // 2 + 20)
            )
            final_score_rect = final_score_text_surface.get_rect(center=(screen_width // 2, screen_height // 2 + 20))

            screen.blit(game_over_text_surface, game_over_rect)
            screen.blit(final_score_text_surface, final_score_rect)

    def trigger_game_over(self):
        self.is_game_over = True
