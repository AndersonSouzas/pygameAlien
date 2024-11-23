from utils import PlayerAction
from typing import List


class PlayerState:
    def __init__(self):
        self._player_action: PlayerAction = PlayerAction.IDLE
        self._player_position_x: float = 0
        self._player_position_y: float = 0
        self._sprite_index: int = 0
        self._animation_update_time: float = 0

    def get_player_action(self) -> PlayerAction:
        return self._player_action

    def set_player_action(self, player_action: PlayerAction):
        self._player_action = player_action

    def get_player_position(self) -> List[float]:
        return [self._player_position_x, self._player_position_y]

    def get_player_position_x(self) -> float:
        return self._player_position_x

    def set_player_position_x(self, player_position_x: float):
        self._player_position_x = player_position_x

    def set_player_position_y(self, player_position_y: float):
        self._player_position_y = player_position_y

    def get_player_position_y(self) -> float:
        return self._player_position_y

    def set_player_position(self, position_x: float, position_y: float):
        self._player_position_x = position_x
        self._player_position_y = position_y

    def get_animation_update_time(self) -> float:
        return self._animation_update_time

    def set_animation_update_time(self, animation_update_time: float):
        self._animation_update_time = animation_update_time
