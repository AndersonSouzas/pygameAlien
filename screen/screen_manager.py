from pygame import Surface
from typing import List
from pygame.event import Event
from .game_screen import GameScreen
from .main_menu_screen import MainMenuScreen
from .screen import ScreenType


class ScreenManager:
    def __init__(self, screen: Surface):
        self.screen = screen
        self.screens: dict = {
            f'{ScreenType.MAIN_MENU.name}': MainMenuScreen(screen),
            f'{ScreenType.GAME_SCREEN.name}': GameScreen(screen),
        }
        self._current_screen: str = ScreenType.MAIN_MENU.name

    def handle_events(self, events: List[Event]):
        next_screen: str = self.screens[self._current_screen].handle_events(events)
        if next_screen:
            self._current_screen = next_screen

    def update(self):
        self._screens[self._current_screen].update()

    def render(self):
        self._screens[self._current_screen].render()
