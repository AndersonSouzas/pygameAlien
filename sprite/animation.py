from pygame.key import get_pressed
from inputs import Keymap
from utils import PlayerAction, PlayerColor
from state import PlayerState
from os import path, listdir
from typing import List
from pygame import image, Surface, transform


class Animation:
    def __init__(self, player_state: PlayerState, player_color: PlayerColor, speed: float, scale: float,
                 screen: Surface):
        self._player = player_state
        self._speed = speed
        self._scale = scale
        self._screen: Surface = screen
        self.player_color = PlayerColor
        self._keymap = Keymap.Player
        self._sprites: dict = {}
        self._current_sprites = []
        self._current_sprite_index = 0
        self._time_since_last_frame = 0

        for action in PlayerAction:
            self._sprites[action] = self._load_sprites(player_color.value, action)

    def _load_sprites(self, player_color: PlayerColor, player_action: PlayerAction) -> List[Surface]:
        sprites: List[Surface] = []
        base_path = path.dirname(path.dirname(__file__))
        sprites_path: str = f'assets/images/sprites/alien/{player_color}/{player_action.name}'
        sprites_path = path.join(base_path, sprites_path)

        if not path.exists(sprites_path):
            raise FileNotFoundError(f"O diretório de sprites {sprites_path} não foi encontrado.")

        files: List[str] = listdir(sprites_path)

        for file in files:
            sprite: Surface = image.load(f'{sprites_path}/{file}')
            width, height = sprite.get_size()
            scaled_sprite: Surface = transform.scale(sprite, (int(width * self._scale), int(height * self._scale)))
            sprites.append(scaled_sprite)
        return sprites

    def update(self, delta_time: float):
        self._time_since_last_frame += delta_time
        keys = get_pressed()

        dx, dy = 0, 0
        current_action = PlayerAction.IDLE

        if keys[self._keymap.UP.value]:
            dy -= self._speed * delta_time
            current_action = PlayerAction.MOVE_UP
        elif keys[self._keymap.DOWN.value]:
            dy += self._speed * delta_time
            current_action = PlayerAction.MOVE_DOWN
        elif keys[self._keymap.LEFT.value]:
            dx -= self._speed * delta_time
            current_action = PlayerAction.MOVE_BACKWARD
        elif keys[self._keymap.RIGHT.value]:
            dx += self._speed * delta_time
            current_action = PlayerAction.MOVE_FORWARD

        self._player.set_player_action(current_action)

        player_x, player_y = self._player.get_player_position()
        new_x = player_x + dx
        new_y = player_y + dy
        self._player.set_player_position(new_x, new_y)

        if self._time_since_last_frame >= self._speed:
            self._current_sprite_index = (self._current_sprite_index + 1) % len(self._current_sprites)
            self._time_since_last_frame = 0

        self._current_sprites = self._sprites[self._player.get_player_action()]

    def render(self):
        if not self._current_sprites:
            raise ValueError(f"Nenhum sprite carregado para a ação {self._player.get_player_action()}.")

        current_sprite = self._current_sprites[self._current_sprite_index]

        position = self._player.get_player_position()
        self._screen.blit(current_sprite, position)
