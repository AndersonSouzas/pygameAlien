from enum import Enum
from pygame import (K_w, K_a, K_s, K_d)

class Keymap:
    class Player(Enum):
        UP = K_w
        DOWN = K_s
        LEFT = K_a
        RIGHT = K_d
