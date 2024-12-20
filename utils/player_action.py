from enum import Enum


class PlayerAction(Enum):
    IDLE = 'IDLE'
    MOVE_FORWARD = 'MOVE_FORWARD'
    MOVE_BACKWARD = 'MOVE_BACKWARD'
    MOVE_UP = 'MOVE_UP'
    MOVE_DOWN = 'MOVE_DOWN'
