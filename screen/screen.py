from enum import Enum
from pygame import Surface
from typing import List
from pygame.event import Event
from abc import ABC, abstractmethod


class ScreenType(Enum):
    MAIN_MENU = 'MAIN_MENU'
    GAME_SCREEN = 'GAME_SCREEN'


class Screen(ABC):
    def __init__(self, screen: Surface):
        self.screen = screen

    @abstractmethod
    def handle_events(self, events: List[Event]) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass
