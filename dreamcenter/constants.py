import pygame as pg
from typing import Dict, Tuple
from itertools import chain

DESIRED_FPS = 60

# Tile width and height.
TILE_HEIGHT = 50
TILE_WIDTH = 50

# Number of tiles in the Y and X axes
TILES_Y = 20
TILES_X = 32

FONT_NAME = None
FONT_SIZE = 20

SCREENRECT = pg.Rect(0, 0, TILE_WIDTH * TILES_X, TILE_HEIGHT * TILES_Y)

MOUSE_LEFT, MOUSE_MIDDLE, MOUSE_RIGHT = 1, 2, 3

SPRITES = {
    "edwardo": "edwardo.png",
    "edwardowithgun": "edwardowithgun.png",
    "background": "background.png",
    "logo": "logo.png",
    "edit_background": "edit_background.png",
    "play_background": "play_background.png",
    "blank": "blank.png",
    "bricks1": "bricks1.png",
    "bloody_floor": "bloody_floor.png",
    "projectile": "projectile.png",
    "skeleton": "Skeleton_Walk_000.png",
}

ANIMATIONS = {
    "projectile_explode": ["projectile_{:003}".format(frame) for frame in range(1, 3 + 1)],
    "skeleton_walk": ["Skeleton_Walk_{:003}".format(frame) for frame in range(1, 3 + 1)],
    "skeleton_death": ["Skeleton_Death_{:003}".format(frame) for frame in range(1, 3 + 1)],
    "skeleton_walk": ["Skeleton_Walk_{:003}".format(frame) for frame in range(1, 3 + 1)],
    "skeleton_stopped": ["Skeleton_Stopped_{:003}".format(frame) for frame in range(1, 3 + 1)],
}

for animation in chain.from_iterable(ANIMATIONS.values()):
    SPRITES[animation] = f"{animation}.png"

# Holds the converted and imported sprite images. The key is a tuple
# of (flipped_x, flipped_y, sprite_name)
IMAGE_SPRITES: Dict[Tuple[bool, bool, str], pg.Surface] = {}

ALLOWED_BG = [
    "bricks1",
    "bloody_floor",
    "blank",
]

ALLOWED_ENEMY = [
    "skeleton",
]

WALLS = [
    "bricks1",
]

TILE_MAPS = {
    "bricks1": ((0, 0), (0, 0)),
    "bloody_floor": ((1, 1), (1, 1)),
    "blank": ((1, 1), (1, 1)),
}

SOUNDS = {}

KEY_ENEMY = 0
KEY_BACKGROUND = 1
KEY_SHRUB = 2

CACHE = {}


