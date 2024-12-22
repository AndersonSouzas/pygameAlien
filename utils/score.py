import pygame


class Score:
    def __init__(self, font_path=None, font_size=36, color=(164, 167, 235)):
        self.score = 0
        self.is_game_over = False
        self.color = color
        self.font = pygame.font.Font(font_path, font_size)

    def add_score(self, points: int):
        if not self.is_game_over:
            self.score += points

    def render_score(self, screen: pygame.Surface) -> None:
        score_text = self.font.render(f"Score: {self.score}", True, self.color)
        screen.blit(score_text, (10, 10))

    def render_game_over(self, screen: pygame.Surface) -> None:

        if self.is_game_over:
            game_over_text = self.font.render("Game Over", True, self.color)
            final_score_text = self .font.render(f"Final Score: {self.score}", True, self.color)

            screen_width, screen_height = screen.get_size()
            
            game_over_rect = game_over_text.get_rect(center=(screen_width//2, screen_height//2 - 40))
            final_score_rect = final_score_text.get_rect(center=(screen_width//2, screen_height//2 + 20))

            screen.blit(game_over_text, game_over_rect)
            screen.blit(final_score_text, final_score_rect)

    def trigger_game_over(self):
        self.is_game_over = True
