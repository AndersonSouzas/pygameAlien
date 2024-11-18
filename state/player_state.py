from typing import List


class PlayerState:
    def __init__(self):
        self._player_position_x: float = 0
        self._player_position_y: float = 0

    def get_player_position(self) -> List[float]:
        return [self._player_position_x, self._player_position_y]

    def get_player_position_x(self) -> float:
        return self._player_position_x

    def get_player_position_y(self) -> float:
        return self._player_position_y

    def set_player_position(self, position_x: float, position_y: float):
        self._player_position_x = position_x
        self._player_position_y = position_y
