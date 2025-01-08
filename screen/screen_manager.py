from pygame import Surface
from typing import List
from pygame.event import Event
from .game_screen import GameScreen
from .main_menu_screen import MainMenuScreen
from .screen import ScreenType
import sys


class ScreenManager:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.screens: dict = {
            f'{ScreenType.MAIN_MENU.value}': MainMenuScreen(screen,
                                                            on_start=self.start_game,
                                                            on_quit=self.quit_game),
            f'{ScreenType.GAME_SCREEN.value}': GameScreen(screen,
                                                          on_quit=self.quit_game),
        }
        self.current_screen: str = ScreenType.MAIN_MENU.value

    def set_current_screen(self, screen_name: str):
        if screen_name in self.screens:
            self.current_screen = screen_name
        else:
            raise ValueError(f'{screen_name} is not a valid screen')

    def handle_events(self, events: List[Event]):
        next_screen: str = self.screens[self.current_screen].handle_events(events)
        if next_screen:
            self.set_current_screen(next_screen)

    def update(self) -> None:
        self.screens[self.current_screen].update()

    def render(self) -> None:
        self.screens[self.current_screen].render()

    def start_game(self):
        self.set_current_screen(ScreenType.GAME_SCREEN.value)

    @staticmethod
    def quit_game():
        sys.exit()
